const puppeteer = require('puppeteer');
const path = require('path');

(async () => {
  const browser = await puppeteer.launch({
    executablePath: 'C:/Users/robert/.cache/puppeteer/chrome/win64-146.0.7680.66/chrome-win64/chrome.exe'
  });
  const page = await browser.newPage();
  const htmlPath = path.resolve(__dirname, 'USP - Pregled i Objasnjenja.html');
  const fileUrl = 'file:///' + htmlPath.split('\\').join('/');
  await page.goto(fileUrl, { waitUntil: 'networkidle0' });
  await page.pdf({
    path: path.resolve(__dirname, 'USP - Pregled i Objasnjenja.pdf'),
    format: 'A4',
    margin: { top: '20mm', bottom: '20mm', left: '15mm', right: '15mm' },
    printBackground: true
  });
  await browser.close();
  console.log('PDF generated.');
})();
