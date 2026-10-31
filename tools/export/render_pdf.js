// Render a pandoc-produced HTML file to PDF, rendering Mermaid diagrams first.
// Usage: node render_pdf.js <input.html> <output.pdf> <mermaid.min.js>
const { chromium } = require('playwright');

(async () => {
  const [, , inHtml, outPdf, mermaidJs] = process.argv;
  const browser = await chromium.launch({ args: ['--no-sandbox'] });
  const page = await browser.newPage();
  await page.goto('file://' + inHtml, { waitUntil: 'load' });

  const n = await page.evaluate(() =>
    document.querySelectorAll('pre.mermaid, code.mermaid, .mermaid').length);
  if (n > 0) {
    await page.addScriptTag({ path: mermaidJs });
    const res = await page.evaluate(async () => {
      try {
        // pandoc may wrap mermaid as <pre class="mermaid"><code>…</code></pre>;
        // collapse each target to a plain text node so mermaid parses cleanly.
        document.querySelectorAll('pre.mermaid, .mermaid').forEach(el => {
          el.textContent = el.textContent;
          el.removeAttribute('data-processed');
        });
        window.mermaid.initialize({ startOnLoad: false, theme: 'default', securityLevel: 'loose' });
        await window.mermaid.run({ querySelector: 'pre.mermaid, .mermaid' });
        return 'rendered ' + document.querySelectorAll('.mermaid svg').length + ' svg';
      } catch (e) { return 'err:' + e.message; }
    });
    console.log('mermaid:', res, '(targets=' + n + ')');
  }
  await page.waitForTimeout(1200);
  await page.pdf({
    path: outPdf, format: 'A4', printBackground: true,
    margin: { top: '0', bottom: '0', left: '0', right: '0' },
    displayHeaderFooter: true,
    headerTemplate: '<span></span>',
    footerTemplate: '<div style="width:100%;font-size:8px;color:#888;padding:0 14mm;display:flex;justify-content:space-between;"><span>AutoAgentAI — Documentation</span><span class="pageNumber"></span></div>',
  });
  await browser.close();
  console.log('PDF written:', outPdf);
})().catch(e => { console.error(e); process.exit(1); });
