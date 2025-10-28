# generate_qr.py
# Usage: python generate_qr.py "https://your-hosted-url.example/puffin"
import sys
try:
    import qrcode
except ImportError:
    print("Please install qrcode: pip install qrcode[pil]")
    sys.exit(1)
url = sys.argv[1] if len(sys.argv)>1 else "https://example.com/puffin"
img = qrcode.make(url)
img.save("assets/qr_generated.png")
print("Saved assets/qr_generated.png")
