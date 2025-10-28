北極海鸚 AR 展示 — 專案說明
========================

檔案結構:
- index.html        : 主頁面 (請上傳至網路以供手機掃描)
- models/puffin.glb : (請放入你的 puffin .glb 模型)
- assets/           : 圖示與 QR 的位置
- README.html       : 此文件的 HTML 版本

說明:
1) 取得 3D 模型
   - 建議來源: Sketchfab, Poly Haven, Clara.io 或其他可商用/非商用明確授權的網站。
   - 下載後把檔案放到 models/puffin.glb

2) 本地測試
   - 直接在桌機上開啟 index.html 可以測試旋轉互動，但部分瀏覽器會限制 AR 功能。
   - 要使用手機 AR: 將整個專案上傳至 GitHub Pages 或 Netlify，取得 https://... 的網址，再用手機掃描 QR。

3) 部署到 GitHub Pages（簡易步驟）
   - 建立一個 GitHub repository，把整個專案上傳（包含 models 資料夾）。
   - 在 repo 的 Settings -> Pages 中選擇 main branch 的 / (root) 作為發佈來源。
   - 等待幾分鐘，就會產生 https://<你的帳號>.github.io/<repo> 的網址。

4) 產生 QR code
   - 本專案內含一個簡易 Python 腳本 (generate_qr.py)：你可以用它產生指向你上傳後網址的 QR 圖檔。
   - 如果你在本地電腦，可以安裝 qrcode: pip install qrcode[pil]
   - 也可以使用線上 QR 產生器 (例如 qr-code-generator.com) 複製你的網址貼上即可。

注意事項:
- 我無法自動為你下載 3D 模型（網路瀏覽在此環境被禁用），請自行下載並放入 models/puffin.glb。
- 若你想要，我可以在你提供模型檔後把 model 檔名/路徑整合進 index.html 並重新打包。
