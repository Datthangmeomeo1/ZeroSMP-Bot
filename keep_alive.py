from flask import Flask, render_template_string
from threading import Thread

app = Flask('')

bot_status = {
    "bot1": "🌙 Đang chạy (Idle)",
    "bot2": "🌙 Đang chạy (Idle)",
    "bot3": "🌙 Đang chạy (Idle)"
}

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Quản Lý Discord Bot - ZeroSMP</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #0f172a; color: #f8fafc; text-align: center; padding: 50px; }
        .card { background: #1e293b; padding: 30px; border-radius: 12px; display: inline-block; box-shadow: 0 4px 20px rgba(0,0,0,0.5); width: 400px; }
        h1 { color: #38bdf8; font-size: 24px; margin-bottom: 20px; }
        .status-box { background: #334155; padding: 15px; border-radius: 8px; margin-bottom: 20px; text-align: left; }
        .status-item { margin: 10px 0; font-size: 16px; }
    </style>
</head>
<body>
    <div class="card">
        <h1>🎮 Quản Lý Bot ZeroSMP</h1>
        <div class="status-box">
            <div class="status-item"><b>Bot 1 (Admin):</b> {{ status.bot1 }}</div>
            <div class="status-item"><b>Bot 2 (Nhạc & Mod):</b> {{ status.bot2 }}</div>
            <div class="status-item"><b>Bot 3 (General):</b> {{ status.bot3 }}</div>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, status=bot_status)

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive(on_callback=None, off_callback=None):
    t = Thread(target=run, daemon=True)
    t.start()