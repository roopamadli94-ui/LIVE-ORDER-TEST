
import requests
import pandas as pd
from datetime import datetime, timedelta
import time
import io
import threading
import webbrowser
import os

def input_with_default(prompt, default):
    inp = input(f"{prompt} [{default}]: ") or default
    return inp

def get_user_inputs():
    import http.server
    import socketserver
    import threading
    import webbrowser

    user_data = {}

    HTML_FORM = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Golden Fish Strategy | TIME LINE INVESTMENTS PVT LTD</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css">
    <style>
        :root {
            --glass-bg: rgba(255, 255, 255, 0.10);
            --glass-border: rgba(255,255,255,0.27);
            --primary: #1d4ed8;
            --gold: #ffd700;
            --gold-gradient: linear-gradient(135deg, #2563eb 0%, #fdc700 100%);
            --shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.22);
            --input-bg: rgba(255,255,255,0.21);
            --input-border: #e0e4f7;
        }
        * { box-sizing: border-box; font-family: 'Poppins', sans-serif; }
        body {
            margin:0; padding:0;
            min-height: 100vh;
            width: 100vw;
            background: var(--gold-gradient);
            position: relative;
            overflow-x: hidden;
        }
        /* Watermark candlestick chart */
        body::before {
            content: '';
            display: block;
            position: absolute;
            left: 10%; 
            top: 37%; 
            width: 750px; height: 400px;
            background: url('https://svgshare.com/i/18qX.svg') no-repeat center center;
            background-size: contain;
            opacity: 0.11;
            z-index: 1;
            pointer-events: none;
            filter: blur(0.3px);
        }
        .bg-floating {
            position: absolute;
            z-index: 2;
            pointer-events: none;
        }
        .fish {
            width: 80px; height: 80px;
            left: 7%; top: 72%;
            animation: floatFish 9s infinite linear alternate;
        }
        .circle1 {
            left: 15%; top: 15%; width: 90px; height: 90px; 
            background: rgba(253, 199, 0, 0.24);
            border-radius: 50%;
            filter: blur(1px);
            animation: float1 18s infinite alternate;
        }
        .circle2 {
            right: 6%; top: 30%; width: 60px; height: 60px; 
            background: rgba(37, 99, 235, 0.11);
            border-radius: 50%;
            filter: blur(1.2px);
            animation: float2 13s infinite alternate;
        }
        .circle3 {
            left: 60%; bottom: 8%; width: 50px; height: 50px; 
            background: rgba(37, 99, 235, 0.15);
            border-radius: 80% 60% 70% 90%;
            filter: blur(0.5px);
            animation: float3 15s infinite alternate;
        }
        @keyframes floatFish { 0%{ top: 72%; left: 7%; } 100%{ top: 67%; left: 12%; } }
        @keyframes float1 { 0%{ top: 15%; left: 15%; } 100%{ top: 18%; left: 18%; } }
        @keyframes float2 { 0%{ top: 30%; right: 6%; } 100%{ top: 26%; right: 3%; } }
        @keyframes float3 { 0%{ left: 60%; bottom: 8%; } 100%{ left: 63%; bottom: 5%; } }

        .main-layout {
            z-index: 10; /* above candlestick chart and floaters */
            position: relative;
            width: 100vw; min-height: 100vh; 
            display: flex; flex-direction: row;
            justify-content: center;
            align-items: stretch;
            gap: 0;
        }
        .left-panel {
            flex: 1 0 55%;
            min-width: 340px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: flex-end;
            padding: 60px 3vw 60px 0;
            position: relative;
        }
        .right-panel {
            flex: 0 1 45%;
            min-width: 320px;
            display: flex;
            justify-content: flex-start;
            align-items: center;
            padding: 60px 0 60px 3vw;
        }
        .fish-illustration {
            width: 170px;
            margin-bottom: 32px;
            filter: drop-shadow(0px 16px 40px #161a2833);
        }
        .company-logo {
            width: 52px; height: 52px;
            border-radius: 22px;
            margin-bottom: 16px;
            background: linear-gradient(135deg,#fdc700,#2563eb);
            display: flex; align-items: center; justify-content: center;
            font-size: 2.1rem; color: #fff; font-weight: bold;
            box-shadow: 0 5px 18px 0 rgba(253, 199, 0, 0.15);
        }
        .left-content-group {
            background: var(--glass-bg);
            border-radius: 30px;
            padding: 42px 36px;
            box-shadow: var(--shadow);
            border: 1.5px solid var(--glass-border);
            min-width: 340px;max-width: 480px;
            display: flex; flex-direction: column;
            align-items: flex-end;
            position: relative;
            z-index: 3;
            backdrop-filter: blur(21px);
        }
        .left-content-group h1 {
            margin-bottom: 10px;
            color: #133c6e;
            font-size: 1.6rem;
            font-weight: 700;
            letter-spacing: 1px;
            text-align: right;
        }
        .golden-text { color: #fdc700; font-weight: 700; }
        .marketing-text {
            text-align: right;
            margin: 17px 0 0 0;
            color: #695e38;
            font-size: 1.05rem;
            font-weight: 600;
            letter-spacing: 0.1px;
        }
        .features {
            width: 102%;
            margin: 38px 0 10px 0;
            display: flex; flex-wrap: wrap; gap: 20px 23px;
        }
        .feature-card {
            flex: 1 1 41%;
            min-width: 170px;
            background: var(--glass-bg);
            border: 1.2px solid var(--glass-border);
            border-radius: 19px;
            box-shadow: 0 3px 16px 0 rgba(37,99,235,0.09);
            padding: 19px 17px 16px 19px;
            margin-bottom: 10px;
            display: flex; align-items: flex-start; gap: 0.9em;
            backdrop-filter: blur(7px);
        }
        .feature-card i { font-size: 1.78rem; color: #1d4ed8; margin-right: 6px;}
        .feature-title {
            color: #1e293b; font-size: 1.07em;font-weight: 700;margin-bottom:2px;
        }
        .feature-desc { color: #475569;font-size: 0.98em;font-weight: 500;}
        /* Right Panel: Glass Login Card */
        .login-card {
            width: 100%; max-width: 390px; min-width: 285px;
            background: var(--glass-bg);
            border: 1.5px solid var(--glass-border);
            border-radius: 32px;
            box-shadow: var(--shadow);
            padding: 36px 32px 31px 32px;
            display: flex; flex-direction: column;
            align-items: center;
            z-index: 10;
            backdrop-filter: blur(19px);
        }
        .login-card h2 {
            color: #133c6e; font-weight: 700; margin-bottom: 8px; font-size: 1.21rem;
            text-align: center;
        }
        .login-card .welcome {
            color: #475569;
            font-size: 1.09rem;
            margin-bottom: 20px;
            font-weight: 500;
            text-align: center;
        }
        .form-group {
            width: 100%;
            margin-bottom: 23px;
            position: relative;
        }
        .input-icon {
            position: absolute;
            left: 13px;
            top: 53%;
            transform: translateY(-50%);
            color: #2563eb;
            font-size: 1.14em;
            opacity: 0.85;
            pointer-events: none;
        }
        .show-hide-btn {
            position: absolute;
            right: 9px;
            top: 50%;
            transform: translateY(-50%);
            background: none;
            border: none;
            color: #64748b;
            cursor: pointer;
            font-size: 1.12em;
            outline: none;
            padding: 0;
        }
        input[type="password"], input[type="text"], input[type="number"] {
            width: 100%;
            font-size: 1.14em;
            border-radius: 20px;
            background: var(--input-bg);
            border: 1.4px solid var(--input-border);
            padding: 15px 45px 15px 38px;
            margin-top: 1px;
            font-weight: 500;
            color: #1e293b;
            box-shadow: 0 1px 4px rgba(30,64,175,0.07);
            transition: border-color .21s, box-shadow .21s;
        }
        input[type="password"]:focus, input[type="text"]:focus, input[type="number"]:focus {
            border-color: #fdc700;
            outline: none;
            box-shadow: 0 1px 8px #ffd70010;
        }
        label {
            display: block;
            font-size: 0.99em;
            font-weight: 600;
            color: #334155;
            margin-bottom: 7px;
            margin-left: 3px;
        }
        .required {
            color: #ef4444;
            font-size: 1.07em;
        }
        .primary-btn {
            width: 100%;
            border: none;
            border-radius: 20px;
            background: linear-gradient(90deg, #fdc700, #2563eb);
            color: #fff;
            font-size: 1.13rem;
            font-weight: 700;
            padding: 17px 0;
            cursor: pointer;
            margin-top: 6px;
            margin-bottom: 7px;
            transition: filter .19s, transform .16s, box-shadow .14s;
            box-shadow: 0px 4px 22px 0px #fdc70038, 0 3px 13px #2563eb18;
        }
        .primary-btn:hover {
            filter: brightness(1.07) drop-shadow(0 8px 22px #2563eb4a);
            transform: translateY(-2px) scale(1.01);
        }
        .footer {
            margin-top: 33px;
            padding-top: 13px;
            width: 100%;
            border-top: 1px solid #e2e8f0bb;
            text-align: center;
            color: #64748b;
            font-size: 0.96em;
            letter-spacing: 0.09px;
            text-shadow: 0 1px 3px #fff1;
        }
        .version {
            margin-top: 10px;
            display: inline-block;
            background: linear-gradient(90deg, #dbeafe, #fefce8);
            color: #1d4ed8;
            padding: 6px 16px;
            border-radius: 16px;
            font-size: 1em;
            font-weight: 600;
            box-shadow: 0 1px 5px #1d4ed813;
        }
        /* Responsive adjustments */
        @media (max-width: 1100px) {
            .main-layout { flex-direction: column; }
            .left-panel, .right-panel { 
                padding: 36px 0 22px 0; 
                justify-content: flex-start; align-items: center; 
            }
            .left-content-group { padding: 36px 19px; }
            .right-panel { padding: 8px 0 36px 0;}
        }
        @media (max-width: 600px) {
            .main-layout { flex-direction: column; min-width: 0; }
            .left-panel, .right-panel {
                min-width: 0; width: 100vw !important;
                padding: 21px 0 !important;
            }
            .left-content-group, .login-card { min-width: 0; width: 92vw; max-width: 98vw;}
            .features { flex-direction: column; gap: 7px; margin: 18px 0 9px 0;}
            .feature-card { padding: 13px 10px; min-width: 120px; }
            .fish-illustration { width: 100px; }
        }
    </style>
    </head>
    <body>
        <!-- floating/fish/circle SVGs for effect -->
        <div class="bg-floating fish">
            <svg width="86" height="86" viewBox="0 0 80 80" fill="none">
                <ellipse cx="40" cy="46" rx="17" ry="27" fill="url(#goldfish)"/>
                <ellipse cx="62" cy="30" rx="12" ry="5" fill="#ffe28a"/>
                <ellipse cx="17" cy="45.5" rx="9.5" ry="19.5" fill="#fada48" fill-opacity="0.36"/>
                <ellipse cx="29" cy="64" rx="6" ry="6" fill="#fdc700" fill-opacity="0.56"/>
                <ellipse cx="40" cy="52" rx="7.5" ry="15.5" fill="#ffd700" fill-opacity="0.37"/>
                <ellipse cx="48" cy="44" rx="3" ry="2" fill="#e2a300"/>
                <ellipse cx="38" cy="43" rx="3" ry="2" fill="#fdc700"/>
                <ellipse cx="41" cy="41" rx="2" ry="1.2" fill="#d08100"/>
                <ellipse cx="28" cy="46" rx="4.5" ry="3.1" fill="#ffe592"/>
                <ellipse cx="56" cy="55" rx="7.5" ry="7" fill="#eab308" fill-opacity="0.43"/>
                <circle cx="36.5" cy="34.5" r="2" fill="#175b76"/>
                <defs>
                    <linearGradient id="goldfish" x1="20" y1="26" x2="60" y2="76" gradientUnits="userSpaceOnUse">
                    <stop stop-color="#ffe28a"/>
                    <stop offset="1" stop-color="#fdc700"/>
                    </linearGradient>
                </defs>
            </svg>
        </div>
        <div class="bg-floating circle1"></div>
        <div class="bg-floating circle2"></div>
        <div class="bg-floating circle3"></div>

        <div class="main-layout">
          <!-- Left panel: Company, logo, features, marketing -->
          <div class="left-panel">
            <div class="left-content-group">
              <div class="company-logo"> <span style="font-size:2.7rem;">🐟</span> </div>
              <div style="text-align:right;font-size:18px;color:#1e293b; font-weight:600;">TIME LINE INVESTMENTS<br/>PVT LTD</div>
              <h1>Golden Fish <span class="golden-text">Strategy</span></h1>
              <div class="marketing-text">
                The modern way to trade: Lightning-fast execution, AI-powered insights, and smart automation.<br>
                <span style='color:#fdc700;'>Swim with the market. Trade with confidence.</span>
              </div>
              <div class="features">
                <div class="feature-card">
                  <i class="bi bi-lightning-charge"></i>
                  <div>
                    <div class="feature-title">Automated Trading</div>
                    <div class="feature-desc">Let the algorithm catch your opportunities 24/7.</div>
                  </div>
                </div>
                <div class="feature-card">
                  <i class="bi bi-graph-up-arrow"></i>
                  <div>
                    <div class="feature-title">Live Market Analysis</div>
                    <div class="feature-desc">Real-time market scanning and candlestick charting.</div>
                  </div>
                </div>
                <div class="feature-card">
                  <i class="bi bi-shield-check"></i>
                  <div>
                    <div class="feature-title">Risk Management</div>
                    <div class="feature-desc">Built-in stoploss and position controls.</div>
                  </div>
                </div>
                <div class="feature-card">
                  <i class="bi bi-robot"></i>
                  <div>
                    <div class="feature-title">Smart Entry &amp; Exit</div>
                    <div class="feature-desc">AI chooses where to enter and when to exit.</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <!-- Right panel: Glassmorphism login/form card -->
          <div class="right-panel">
            <form class="login-card" method="POST" autocomplete="off" onsubmit="return handleFormSubmit(event)">
                <h2>Welcome to <span class="golden-text">Golden Fish</span></h2>
                <div class="welcome">Configure strategy &amp; get started instantly!</div>
                <!-- Access Token -->
                <div class="form-group">
                    <label for="access_token">
                        <i class="bi bi-fingerprint" style="color:#ffd700; margin-right:5px"></i>
                        Dhan Access Token <span class="required">*</span>
                    </label>
                    <i class="input-icon bi bi-key"></i>
                    <input type="password" id="access_token" name="access_token" required placeholder="Enter your access token">
                    <button type="button" class="show-hide-btn" onclick="togglePwd(this, 'access_token')">
                        <i class="bi bi-eye"></i>
                    </button>
                </div>
                <!-- Stop Loss -->
                <div class="form-group">
                    <label for="stoploss_points">
                        <i class="bi bi-shield-check" style="color:#2563eb; margin-right:5px"></i>
                        Stop Loss (Points) <span class="required">*</span>
                    </label>
                    <i class="input-icon bi bi-exclamation-triangle"></i>
                    <input type="number" id="stoploss_points" name="stoploss_points" step="0.01" min="0.01" value="30" required>
                </div>
                <!-- Timeframe -->
                <div class="form-group">
                    <label for="timeframe">
                        <i class="bi bi-clock-history" style="color:#2563eb; margin-right:5px"></i>
                        Candle Timeframe <span class="required">*</span>
                    </label>
                    <i class="input-icon bi bi-clock"></i>
                    <input type="number" id="timeframe" name="timeframe" min="1" value="1" required>
                </div>
                <!-- Exit After Candles -->
                <div class="form-group">
                    <label for="exit_candle_count">
                        <i class="bi bi-door-open" style="color:#2563eb; margin-right:5px"></i>
                        Exit After Candles <span class="required">*</span>
                    </label>
                    <i class="input-icon bi bi-box-arrow-right"></i>
                    <input type="number" id="exit_candle_count" name="exit_candle_count" min="1" value="3" required>
                </div>
                <button class="primary-btn" type="submit">
                    <i class="bi bi-play-fill" style="font-size:1.23em;margin-right:8px"></i>Start Strategy
                </button>
                <div class="footer">
                    &copy; 2026 <b>TIME LINE INVESTMENTS PVT LTD</b><br>
                    Professional Algorithmic Trading Solutions
                    <div class="version">
                        Golden Fish Strategy &bull; Version 1.0
                    </div>
                </div>
            </form>
          </div>
        </div>
        <script>
        // Show/Hide Password
        function togglePwd(btn, id) {
            var input = document.getElementById(id);
            if (input.type === "password") {
                input.type = "text";
                btn.innerHTML = '<i class="bi bi-eye-slash"></i>';
            } else {
                input.type = "password";
                btn.innerHTML = '<i class="bi bi-eye"></i>';
            }
            input.focus();
        }
        // Close form and show confirmation on submit (for API use)
        function handleFormSubmit(e) {
            // Will be processed by server, allow submit
            return true;
        }
        </script>
    </body>
    </html>
    """

    class CustomHandler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(HTML_FORM.encode('utf-8'))

        def do_POST(self):
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            params = dict(x.split("=", 1) for x in post_data.split("&"))
            from urllib.parse import unquote_plus
            for k, v in params.items():
                params[k] = unquote_plus(v)
            user_data.update(params)
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"<html><head><script>window.close();</script></head>"
                             b"<body><h3 style='text-align:center;margin-top:70px;color:green;'>Submitted! You may close this tab.</h3></body></html>")
            threading.Thread(target=httpd.shutdown, daemon=True).start()

        def log_message(self, format, *args):
            pass 

    PORT = 58238
    Handler = CustomHandler
    httpd = socketserver.TCPServer(("", PORT), Handler)
    url = f"http://localhost:{PORT}/"

    threading.Timer(0.6, lambda: webbrowser.open(url, new=1)).start()
    print("\nA browser window has opened for input. If not, open this URL:", url)
    print("Waiting for user input...\n")
    httpd.serve_forever()

    access_token = user_data.get("access_token", "").strip()
    while not access_token:
        access_token = input("Enter your Dhan access token [from web form]: ").strip()
    timeframe = user_data.get("timeframe", "1").strip()
    while not timeframe.isdigit() or int(timeframe) < 1:
        timeframe = input("Enter candle timeframe in minutes [from web form]: ") or "1"
    timeframe = int(timeframe)
    stoploss_points = user_data.get("stoploss_points", "30").strip()
    while not stoploss_points.replace(".", "", 1).isdigit():
        stoploss_points = input("Stoploss in points [from web form]: ") or "30"
    stoploss_points = float(stoploss_points)
    exit_candle_count = user_data.get("exit_candle_count", "3").strip()
    while not exit_candle_count.isdigit() or int(exit_candle_count) < 1:
        exit_candle_count = input("Candle count after which to exit (integer) [from web form]: ") or "3"
    exit_candle_count = int(exit_candle_count) + 1

    print(f"\nAccess Token: {'*' * len(access_token)}")
    print(f"Timeframe (minutes): {timeframe}")
    print(f"Stoploss Points: {stoploss_points}")
    print(f"Exit Candle Count: {exit_candle_count}")
    print("==============================\n")
    return access_token, timeframe, stoploss_points, exit_candle_count

def fetch_dhan_scrip_master():
    url = "https://images.dhan.co/api-data/api-scrip-master-detailed.csv"
    try:
        resp = requests.get(url, timeout=12)
        resp.raise_for_status()
        csv_bytes = io.BytesIO(resp.content)
        df = pd.read_csv(csv_bytes)
        df_filtered = df[
            (df['EXCH_ID'].str.lower() == 'nse') &
            (df['INSTRUMENT'].str.lower() == 'optidx') &
            (df['UNDERLYING_SYMBOL'].str.upper() == 'NIFTY')
        ].copy()
        df_filtered['SM_EXPIRY_DATE'] = pd.to_datetime(df_filtered['SM_EXPIRY_DATE'], errors='coerce')
        df_filtered = df_filtered.dropna(subset=['SM_EXPIRY_DATE'])

        now = datetime.now()
        this_month = now.month
        this_year = now.year

        df_this_month = df_filtered[
            (df_filtered['SM_EXPIRY_DATE'].dt.year == this_year) &
            (df_filtered['SM_EXPIRY_DATE'].dt.month == this_month)
        ].copy()
        if not df_this_month.empty:
            # If first expiry is today, use next expiry, else use min
            today = pd.Timestamp.now().normalize()
            expiries_sorted = df_this_month['SM_EXPIRY_DATE'].sort_values().unique()
            if len(expiries_sorted) > 0 and expiries_sorted[0].normalize() == today:
                if len(expiries_sorted) > 1:
                    first_expiry = expiries_sorted[1]
                else:
                    first_expiry = expiries_sorted[0]
            else:
                first_expiry = expiries_sorted[0] if len(expiries_sorted) > 0 else None
     
            df_ce = df_this_month[(df_this_month['SM_EXPIRY_DATE'] == first_expiry) & (df_this_month['OPTION_TYPE']=='CE')]
            df_pe = df_this_month[(df_this_month['SM_EXPIRY_DATE'] == first_expiry) & (df_this_month['OPTION_TYPE']=='PE')]
        else:
            df_ce = pd.DataFrame()
            df_pe = pd.DataFrame()
        required_columns = [
            "EXCH_ID",
            "SECURITY_ID",
            "DISPLAY_NAME",
            "LOT_SIZE",
            "SM_EXPIRY_DATE",
            "STRIKE_PRICE",
            "TICK_SIZE"
        ]
        df_ce = df_ce[required_columns].copy()
        df_pe = df_pe[required_columns].copy()

        return df_ce, df_pe
    except Exception as ex:
        print(f"Failed to load scrip master: {ex}")
        return pd.DataFrame(), pd.DataFrame()

global df_ce, df_pe
df_ce, df_pe = fetch_dhan_scrip_master()

orderbook = []

def html_table_from_dataframe(df, table_title=None, max_rows=150):
    table_style = """
    <style>
    .data-table {
        font-family: 'Segoe UI', 'Roboto', Arial, sans-serif; 
        border-collapse: collapse; 
        width: 98%; 
        margin: 24px auto 32px auto; 
        background: #fff;
        box-shadow: 0 4px 18px 0 rgba(60,64,67,.12),0 1.5px 6px 0 rgba(60,64,67,.08);
        border-radius: 8px;
        overflow: hidden;
        font-size: 1.08rem;
    }
    .data-table caption {
        caption-side: top; 
        font-size: 1.45rem; 
        padding: 18px 12px 12px 12px; 
        color: #181c32; 
        font-weight: bold; 
        letter-spacing: .01em;
    }
    .data-table th, 
    .data-table td {
        border: 1px solid #e9ecef; 
        padding: 11px 16px;
        text-align: left;
        vertical-align: middle;
        transition: background 0.25s;
    }
    .data-table th {
        background: linear-gradient(90deg, #2563eb 65%, #0ea5e9 100%);
        color: #fff;
        font-weight: 600;
        font-size: 1.12rem;
        letter-spacing: .01em;
        border-bottom: 2.5px solid #1e429f;
    }
    .data-table tr:nth-child(even) {
        background: #f0f6ff;
    }
    .data-table tr:nth-child(odd) {
        background: #f9fbfd;
    }
    .data-table tr:hover {
        background: #e5edfa;
        box-shadow: 0 2px 8px 0 rgba(30,67,159,.06);
        transition: box-shadow 0.2s;
    }
    .data-table td {
        font-size: 1rem;
        color: #23272f;
        border-bottom: 1px solid #e9ecef;
    }
    .data-table th:first-child, .data-table td:first-child {
        border-left: none;
    }
    .data-table th:last-child, .data-table td:last-child {
        border-right: none;
    }
    </style>
    """
    if df.empty:
        return f"{table_style}<b>No data available</b>"
    if max_rows:
        df = df.tail(max_rows)
    table_html = df.to_html(classes="data-table", escape=False, index=False)
    if table_title:
        table_html = table_html.replace('<table border="1" class="dataframe data-table">', f'<table class="data-table"><caption>{table_title}</caption>')
    return table_style + table_html

from flask import Flask, jsonify, render_template_string, request
import threading as _threading

orderbook_app = Flask(__name__)
# add market open time and show current time and Market Closed logic
ORDERBOOK_HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang='en'>
<head>
<meta charset="UTF-8">
<title style="font-family: 'Segoe UI', 'Roboto', Arial, sans-serif; letter-spacing:0.04em; color:#2563eb; font-size:2.1rem; font-weight:700; text-shadow: 0 2px 6px rgba(17, 82, 147, 0.1);">Live Order Book Golden Fish</title>
<script>
function updateOrderbook() {
    fetch('/orderbook_data')
    .then(resp => resp.json())
    .then(data => {
        let html = data['orderbook_html'];
        document.getElementById('orderbook_table').innerHTML = html;
        updateMarketStatus();
    });
}
function pad2(n) { return n < 10 ? "0" + n : n; }
function formatTime(dt) {
    return pad2(dt.getHours()) + ":" + pad2(dt.getMinutes()) + ":" + pad2(dt.getSeconds())
}
function updateMarketStatus() {
    const now = new Date();
    const hours = now.getHours();
    const minutes = now.getMinutes();
    const timeString = formatTime(now);
    document.getElementById('current_time').innerText = "Current Time: " + timeString;
    // Indian stock market closes at 15:15 (3:15 PM)
    let isClosed = (hours > 15) || (hours === 15 && minutes >= 15);
    document.getElementById('market_status').innerHTML = isClosed
        ? "<span style='color:red;font-weight:bold;'>Market Closed</span>"
        : "<span style='color:green;font-weight:bold;'>Market Open</span>";
}
// Improved: Call both functions once on interval, but ensure updateOrderbook is always called even if updateMarketStatus fails.
// This also avoids issues with JS engine/environment where arrow functions or interval callbacks can sometimes behave oddly.

// Use a watchdog: if functions get stuck, forcibly call them.
let forceUpdateOrderbook = false;
let forceUpdateMarketStatus = false;

function safeUpdateOrderbook() {
    try {
        updateOrderbook();
        forceUpdateOrderbook = false;
    } catch (e) {
        console.error("updateOrderbook error:", e);
        forceUpdateOrderbook = true;
    }
}
function safeUpdateMarketStatus() {
    try {
        updateMarketStatus();
        forceUpdateMarketStatus = false;
    } catch (e) {
        console.error("updateMarketStatus error:", e);
        forceUpdateMarketStatus = true;
    }
}

setInterval(function () {
    safeUpdateOrderbook();
    safeUpdateMarketStatus();

    // If either got stuck recently (e.g. exception thrown), forcibly call it again.
    if (forceUpdateOrderbook) {
        try {
            updateOrderbook();
            forceUpdateOrderbook = false;
        } catch (e) {
            // If it still fails, leave as true for next round.
            console.error("FORCED updateOrderbook error (stuck):", e);
        }
    }
    if (forceUpdateMarketStatus) {
        try {
            updateMarketStatus();
            forceUpdateMarketStatus = false;
        } catch (e) {
            console.error("FORCED updateMarketStatus error (stuck):", e);
        }
    }
}, 1000);

window.onload = function () {
    safeUpdateOrderbook();
    safeUpdateMarketStatus();
};
</script>
</head>
<body>
<nav style="
    display: flex;
    align-items: center; 
    justify-content: space-between;
    background: linear-gradient(90deg, #edf2fa 75%, #dbeafe 100%);
    padding: 20px 36px;
    border-radius: 16px; 
    margin-bottom: 30px;
    box-shadow: 0 4px 18px 0 rgba(51, 73, 143, 0.10), 0 1.5px 6px 0 rgba(25, 67, 123, 0.05);
    gap: 30px;
    font-family: 'Segoe UI', 'Roboto', Arial, sans-serif;
">
    <div style="display:flex; flex-direction:column;">
        <span style="font-size:1.7rem; color:#1e293b; font-weight:800; letter-spacing:0.03em; text-shadow: 0 2px 6px rgba(17, 82, 147, 0.09);">
            Live Order Book <span style="color:#2563eb;">Golden Fish</span>
        </span>
        <span style="font-size:1.22rem; color:#4a5568; font-weight:500; margin-top:2px; letter-spacing:0.01em;">
            <span style="color:#083268; font-weight:600;">Time Line Investments Pvt Ltd</span>
        </span>
    </div>
    <div style="display:flex; flex-direction:column; align-items:flex-end; gap:4px;">
        <div id="current_time" style="font-size:1.13rem; color:#1d3557; font-weight:600;"></div>
        <div id="market_status" style="font-size:1.13rem;"></div>
    </div>
</nav>
<div id="orderbook_table">Loading...</div>
</body>
</html>
"""
@orderbook_app.route('/')
def _orderbook_page():
    return render_template_string(ORDERBOOK_HTML_TEMPLATE)
'''
@orderbook_app.route('/orderbook_data')
def _orderbook_data():
    # Extended columns to show targetCandle and targetTime also
    keys = [
        "time", "transactionType", "symbol", "securityId", "strike",
        "orderId", "status", "price", "quantity",
        "stoplossOrderId", "stoplossStatus", "stoplossPrice",
        "targetCandle", "targetTime","lowBreakPoint", "highBreakPoint","exitPrice", "exitTime", "exitSL", "exitReason","SPOT","high vol","VOL IN LOT"
    ]
    html_rows = []
    for od in orderbook:
        row = [str(od.get(k,""))[:30] for k in keys]
        html_rows.append(row)
    df_html_table = pd.DataFrame(
        html_rows, 
        columns=["Time","Type","Symbol","SecurityID","Strike","OrderID","Status","Price","Qty",
                 "SL OrderID","SL Status","SL Price","Target Candle","Target Time","lowBreakPoint", "highBreakPoint","exitPrice", "exitTime", "exitSL", "exitReason","SPOT","high vol","VOL IN LOT"])
    orderbook_html = html_table_from_dataframe(df_html_table, "Order Book")
    return jsonify(orderbook_html=orderbook_html)

'''
@orderbook_app.route('/orderbook_data')
def _orderbook_data():
    import datetime
    import os

    # Extended columns to show targetCandle and targetTime also
    keys = [
        "time", "transactionType", "symbol", "securityId", "strike",
        "orderId", "status", "price", "quantity",
        "stoplossOrderId", "stoplossStatus", "stoplossPrice",
        "targetCandle", "targetTime", "lowBreakPoint", "highBreakPoint", "exitPrice", "exitTime", "exitSL", "exitReason", "SPOT", "high vol", "VOL IN LOT"
    ]
    html_rows = []
    for od in orderbook:
        row = [str(od.get(k,""))[:30] for k in keys]
        html_rows.append(row)
    # Create DataFrame for HTML and CSV output
    df_html_table = pd.DataFrame(
        html_rows, 
        columns=["Time","Type","Symbol","SecurityID","Strike","OrderID","Status","Price","Qty",
                 "SL OrderID","SL Status","SL Price","Target Candle","Target Time","lowBreakPoint", "highBreakPoint","exitPrice", "exitTime", "exitSL", "exitReason","SPOT","high vol","VOL IN LOT"]
    )

    # Create filename like "orderbook_YYYYMMDD.csv"
    today_str = datetime.datetime.now().strftime("%Y%m%d")
    csv_filename = f"orderbook_{today_str}.csv"

    # Try updating CSV file, if PermissionError, fallback to a temp file or skip writing
    CSV_WRITE_OK = False
    try:
        df_html_table.to_csv(csv_filename, index=False, encoding='utf-8')
        CSV_WRITE_OK = True
    except PermissionError:
        # If the file is open in Excel or otherwise locked, try writing to a temp fallback file (will overwrite every time)
        fallback_name = f"orderbook_{today_str}_tmp.csv"
        try:
            df_html_table.to_csv(fallback_name, index=False, encoding='utf-8')
            print(f"[Warning] Could not write to {csv_filename} (file open?), wrote to {fallback_name} instead.")
            CSV_WRITE_OK = True
        except Exception as e2:
            print(f"[Warning] Failed to write fallback orderbook CSV ({fallback_name}): {e2}")
            # Don't raise, just move on
    except Exception as e:
        print(f"[Warning] Failed to write {csv_filename}: {e}")
        # Don't raise, just move on

    orderbook_html = html_table_from_dataframe(df_html_table, "Order Book")
    return jsonify(orderbook_html=orderbook_html)

def start_orderbook_flask():
    def run_app():
        orderbook_app.run(port=58888, host='127.0.0.1', debug=False, use_reloader=False)
    threading.Thread(target=run_app, daemon=True).start()

def launch_orderbook_frontend(open_browser=True):
    start_orderbook_flask()
    if open_browser:
        webbrowser.open('http://127.0.0.1:58888', new=1)

def print_orderbook(open_browser=False):
    keys = [
        "time", "transactionType", "symbol", "securityId", "strike",
        "orderId", "status", "price", "quantity",
        "stoplossOrderId", "stoplossStatus", "stoplossPrice",
        "targetCandle", "targetTime",
        "lowBreakPoint", "highBreakPoint",
        "exitPrice", "exitTime", "exitSL", "exitReason","SPOT","high vol","VOL IN LOT"
    ]
    # The original line is not correct as the number of placeholders in the format string (16) does not match the number of column labels (20).
    # Here is the corrected version using 20 placeholders, one for each field:
    header = "{:<20} {:<6} {:<30} {:<12} {:<8} {:<16} {:<12} {:<10} {:<8} {:<14} {:<12} {:<10} {:<14} {:<20} {:<14} {:<14} {:<14} {:<14} {:<14} {:<14}".format(
        "Time", "Type", "Symbol", "SecurityID", "Strike", "OrderID", "Status", "Price", "Qty",
        "SL OrderID", "SL Status", "SL Price", "Target Candle", "Target Time", "lowBreakPoint", "highBreakPoint", "exitPrice", "exitTime", "exitSL", "exitReason","SPOT","high vol","VOL IN LOT"
    )
    if not orderbook:
        print("\n===== ORDERBOOK =====")
        print("No orders placed yet.\n")
        orderbook_html = html_table_from_dataframe(pd.DataFrame(columns=keys), "Order Book")
        with open("orderbook.html", "w", encoding='utf-8') as f:
            f.write(orderbook_html)
        if open_browser:
            webbrowser.open('file://' + os.path.abspath("orderbook.html"))
        return

    print("\n===== ORDERBOOK =====")
    print(header)
    print("-"*len(header))
    html_rows = []
    for od in orderbook:
        row = [str(od.get(k,""))[:30] for k in keys]

        print("{:<20} {:<6} {:<30} {:<12} {:<8} {:<16} {:<12} {:<10} {:<8} {:<14} {:<12} {:<10} {:<14} {:<20} {:<14} {:<14} {:<14} {:<14} {:<14} {:<14}".format(*row))
        html_rows.append(row)
    print("\n")
    df_html_table = pd.DataFrame(
        html_rows, columns=["Time","Type","Symbol","SecurityID","Strike","OrderID","Status","Price","Qty",
                            "SL OrderID","SL Status","SL Price","Target Candle","Target Time","lowBreakPoint", "highBreakPoint","exitPrice", "exitTime", "exitSL", "exitReason","SPOT","high vol","VOL IN LOT"]
    )
    
    orderbook_html = html_table_from_dataframe(df_html_table, "Order Book")
    with open("orderbook.html", "w", encoding='utf-8') as f:
        f.write(orderbook_html)
    if open_browser:
        webbrowser.open('file://' + os.path.abspath("orderbook.html"))

def html_option_chain(df_ce_chain, df_pe_chain, open_browser=False):
    ce_html = html_table_from_dataframe(df_ce_chain, table_title="CE Option Chain", max_rows=None)
    pe_html = html_table_from_dataframe(df_pe_chain, table_title="PE Option Chain", max_rows=None)
    combined_html = f"""<div style='display:flex;gap:40px;'>
    <div style='width:49%'>{ce_html}</div>
    <div style='width:49%'>{pe_html}</div>
    </div>
    """
    oc_file_content = f"""<html><head><meta charset="utf-8"></head>
    <body>
    <h2 style='font-size:26px;margin:20px 0;color:#183152;'>Nifty Option Chain (Live)</h2>
    {combined_html}
    </body>
    </html>
    """
    with open("option_chain.html", "w", encoding='utf-8') as f:
        f.write(oc_file_content)
    print("[Info] Option chain tables written to option_chain.html.")
    if open_browser:
        webbrowser.open('file://' + os.path.abspath("option_chain.html"))
global prev_sl_exit
prev_sl_exit = False

global sl_order_time
sl_order_time = datetime.now().strftime("%Y-%m-%d")

global prev_order_id, prev_security_id
prev_order_id = None
prev_security_id = None

order_placed_data = {}

def live_data(access_token, timeframe, stoploss_points, exit_candle_count, open_browser_on_output=False):
    import requests
    global orderbook
    TICK_SIZE = float(df_ce["TICK_SIZE"].iloc[0]) if not df_ce.empty else 0.0
    #print(TICK_SIZE,"TICK SIZE IS=========================================================")
    expiry_date = ""
    if not df_ce.empty and "SM_EXPIRY_DATE" in df_ce.columns:
        expiry_date = df_ce["SM_EXPIRY_DATE"].min()
    else:
        expiry_date = ""

    df_ce_chain = pd.DataFrame()
    df_pe_chain = pd.DataFrame()
    df_ce_chain_html = ''
    df_pe_chain_html = ''
    order_placed_data = None
    from datetime import datetime
    current_second = datetime.now().second
    try:
        url = "https://api.dhan.co/v2/charts/intraday"
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "access-token": access_token
        }   
        now = datetime.now()
        fifteen_thirty = now.replace(hour=15, minute=20, second=0, microsecond=0)
        if now > fifteen_thirty:
            from_date = fifteen_thirty
        else:
            from_date = now - timedelta(minutes=int(timeframe))
        to_date = now.replace(hour=15, minute=30, second=0, microsecond=0)

        #if current_second == 2 and (datetime.now().hour < 15 or (datetime.now().hour == 15 and datetime.now().minute < 10)):
        if current_second == 2 and (datetime.now().hour > 9 or (datetime.now().hour == 9 and datetime.now().minute >= 15)) and (datetime.now().hour < 15 or (datetime.now().hour == 15 and datetime.now().minute < 10)):
   
            exit_all = True
            order_status_comp = "NOT"
            trade_possible_ce = False
            pe_trade_possible = False
            print("TRADE POSSIBLE NOW", datetime.now().second)
            now = datetime.now()
            fifteen_thirty = now.replace(hour=15, minute=20, second=0, microsecond=0)
            if now > fifteen_thirty:
                from_date = fifteen_thirty
            else:
                from_date = now - timedelta(minutes=3)
            to_date = now.replace(hour=15, minute=30, second=0, microsecond=0)

            user_data = {
                "securityId": "13",
                "exchangeSegment": "IDX_I",
                "instrument": "INDEX",
                "interval": str(timeframe),
                "fromDate": datetime.now().strftime("%Y-%m-%d"),
                "toDate": datetime.now().strftime("%Y-%m-%d")
            }
            ##
            #
            intraday_response = requests.post(url, headers=headers, json=user_data)
            records = intraday_response.json() if intraday_response.status_code == 200 else []
            intraday_df = pd.DataFrame(records)
            if "timestamp" not in intraday_df.columns or intraday_df.empty:
                print("No intraday data returned from API.")
                print_orderbook(open_browser=open_browser_on_output)
                return

            intraday_df = intraday_df.tail(2).reset_index(drop=True)
            intraday_df["timestamp"] = pd.to_datetime(intraday_df["timestamp"], unit="s", utc=True).dt.tz_convert('Asia/Kolkata')
            intraday_df["DATE"] = pd.to_datetime(intraday_df["timestamp"]).dt.date
            intraday_df["TIME"] = pd.to_datetime(intraday_df["timestamp"]).dt.time
            intraday_df["SPOT"] = intraday_df["close"]


            target_time_ce = (datetime.now() - timedelta(minutes=1)).replace(second=0, microsecond=0)
                    # Get only the rows of intraday_df_ce where the 'time' column matches target_time_ce (as time object)
            target_time_ce_time = target_time_ce.time()  # .time() gets HH:MM:SS as time object
            intraday_df["TIME"] = pd.to_datetime(intraday_df["timestamp"]).dt.time
            # Get candle color here
            intraday_df_check = intraday_df[intraday_df["TIME"] == target_time_ce_time]
            print(intraday_df_check)
            
            # Determine candle color: Green (close > open), Red (close < open), Doji (close == open)
            if not intraday_df_check.empty:
                open_price = intraday_df_check.iloc[0]["open"]
                close_price = intraday_df_check.iloc[0]["close"]
                if close_price > open_price:
                    candle_color_spot = "Green"
                elif close_price < open_price:
                    candle_color_spot = "Red"
                else:
                    candle_color_spot = "Doji"
                print(f"Candle color: {candle_color_spot}====================================================>")
            else:
                candle_color = None
                print("No candle found for target time.")

            spot = intraday_df["SPOT"].iloc[-1]
            print(intraday_df)
            #strike price checks
            strike_price = spot
     
            atm_strike = (strike_price//50) * 50
            #atm_strike = round(strike_price / 50) * 50
            print(atm_strike, "ATM STRIKE IS ================================================","spot is =================",spot)
            atm_strike_data = atm_strike + 50

            ce_strikes = [atm_strike_data - 50 * i for i in range(1, 5)]
            pe_strikes = [atm_strike + 50 * i for i in range(1, 5)]

            option_chain_url = "https://api.dhan.co/v2/optionchain"
            option_chain_headers = {
                "Content-Type": "application/json",
                "access-token": access_token,
                "client-id": "1106302772"
            }
            option_chain_payload = {
                "UnderlyingScrip": 13,
                "UnderlyingSeg": "IDX_I",
                "Expiry": str(expiry_date.date()) if expiry_date != "" else ""
            }
            option_chain_resp = requests.post(option_chain_url, headers=option_chain_headers, json=option_chain_payload, timeout=10)
            oc_data = option_chain_resp.json().get('data', {}).get('oc', {})
            ce_list = []
            pe_list = []
            for strike, contracts in oc_data.items():
                strike_float = float(strike)
                if 'ce' in contracts:
                    ce = contracts['ce']
                    ce_row = {"strike": strike_float}
                    for k, v in ce.items():
                        if k == "greeks" and isinstance(v, dict):
                            for gk, gv in v.items():
                                ce_row[f"greek_{gk}"] = gv
                        else:
                            ce_row[k] = v
                    ce_list.append(ce_row)
                if 'pe' in contracts:
                    pe = contracts['pe']
                    pe_row = {"strike": strike_float}
                    for k, v in pe.items():
                        if k == "greeks" and isinstance(v, dict):
                            for gk, gv in v.items():
                                pe_row[f"greek_{gk}"] = gv
                        else:
                            pe_row[k] = v
                    pe_list.append(pe_row)

            import os

            df_ce_chain = pd.DataFrame(ce_list)
            df_pe_chain = pd.DataFrame(pe_list)

            # Save and append df_ce_chain to a CSV file with today's date in the name
            from datetime import datetime

            today_str = datetime.now().strftime("%Y-%m-%d")
            ce_csv_filename = f"df_ce_pe_chain_{today_str}.csv"
            
            if not df_ce_chain.empty or not df_pe_chain.empty:
                html_option_chain(df_ce_chain, df_pe_chain, open_browser=open_browser_on_output)

            if not df_ce_chain.empty:
                df_ce_chain = df_ce_chain.sort_values("strike").reset_index(drop=True)
                df_ce_chain = df_ce_chain[df_ce_chain["strike"].isin(ce_strikes)]
                print(df_ce_chain)
                file_exists = os.path.isfile(ce_csv_filename)
                # Add 'time' column with current complete date time with second
                df_ce_chain['time'] = datetime.now().strftime("%Y-%m-%d")
                df_ce_chain["TYPE"] ="CE"
                df_ce_chain.to_csv(ce_csv_filename, mode='a', index=False, header=not file_exists)
                
                if not df_ce_chain.empty and 'volume' in df_ce_chain.columns:
                    highest_volume = df_ce_chain['volume'].max()
                    df_highest_vol_ce = df_ce_chain[df_ce_chain['volume'] == highest_volume]
                    print("CE dataframe with highest volume:")
                    print(df_highest_vol_ce)
                    

                    strike_point_ce = df_highest_vol_ce['strike'].iloc[0] if not df_highest_vol_ce.empty else None
                    high_vol = df_highest_vol_ce['volume'].iloc[0] if not df_highest_vol_ce.empty else None
                    trade_ce_security = df_ce[df_ce["STRIKE_PRICE"] == strike_point_ce]
                    ce_security = trade_ce_security["SECURITY_ID"].values[0] if not trade_ce_security.empty else None
                    print(ce_security,"got security ID")

                    user_data_ce = {
                        "securityId": str(ce_security),
                        "exchangeSegment": "NSE_FNO",
                        "instrument": "OPTIDX",
                        "interval": str(timeframe),
                        "fromDate": datetime.now().strftime("%Y-%m-%d"),
                        "toDate": datetime.now().strftime("%Y-%m-%d")
                   
                   
                    }
                    #
                    intraday_response_ce = requests.post(url, headers=headers, json=user_data_ce)
                    #print(intraday_response_ce.json())
                    records_ce = intraday_response_ce.json() if intraday_response_ce.status_code == 200 else []
                    
                    intraday_df_ce = pd.DataFrame(records_ce)
                    intraday_df_ce["timestamp"] = pd.to_datetime(intraday_df_ce["timestamp"], unit="s", utc=True).dt.tz_convert('Asia/Kolkata')
                    # Add a 'time' column with the time component (HH:MM:SS) in Asia/Kolkata time
                    intraday_df_ce["time"] = pd.to_datetime(intraday_df_ce["timestamp"]).dt.time
                    
                    #target_time_ce = (datetime.now() - timedelta(minutes=1)).strftime("%H:%M:%S")
                    target_time_ce = (datetime.now() - timedelta(minutes=1)).replace(second=0, microsecond=0)
                    # Get only the rows of intraday_df_ce where the 'time' column matches target_time_ce (as time object)
                    target_time_ce_time = target_time_ce.time()  # .time() gets HH:MM:SS as time object
                    intraday_df_ce = intraday_df_ce[intraday_df_ce["time"] == target_time_ce_time]
                    print(intraday_df_ce)

                    if not intraday_df_ce.empty and {'open', 'close'}.issubset(intraday_df_ce.columns):
                        
                        if len(intraday_df_ce) == 3:
                            last_candle = intraday_df_ce.iloc[1]
                        else:
                            last_candle = intraday_df_ce.iloc[0]
                   
                        open_price = last_candle['open']
                        close_price = last_candle['close']
                        candle_color_ce = "DOJI"
                        if close_price > open_price:
                            print("Last CE candle is GREEN")
                            candle_color_ce = "GREEN"
                        elif close_price < open_price:
                            print("Last CE candle is RED")
                            candle_color_ce = "RED"
                        else:
                            print("Last CE candle is DOJI")
                        #if candle_color_ce == "RED":
                        if candle_color_spot == "Green":
                            print("PLACING ORDER FOR CE") 
                            if len(intraday_df_ce) == 3:
                                high_value_last = intraday_df_ce.iloc[2]['high']
                                high_value_first = intraday_df_ce.iloc[1]['high']
                                #check break point
                                last_candle_low_val = intraday_df_ce.iloc[1]['low']
                                last_candle_high_val = intraday_df_ce.iloc[1]['high']
                            elif len(intraday_df_ce) == 2:
                                high_value_last = intraday_df_ce.iloc[1]['high']
                                high_value_first = intraday_df_ce.iloc[0]['high']
                                #check break point
                                last_candle_low_val = intraday_df_ce.iloc[0]['low']
                                last_candle_high_val = intraday_df_ce.iloc[0]['high']
                            else:
                                #high_value_last = intraday_df_ce.iloc[1]['high']
                                high_value_last = intraday_df_ce.iloc[0]['high']
                                high_value_first = intraday_df_ce.iloc[0]['high']
                                #check break point
                                last_candle_low_val = intraday_df_ce.iloc[0]['low']
                                last_candle_high_val = intraday_df_ce.iloc[0]['high']
                       
                            print(f"high_value_last: {high_value_last}")
                            print(f"high_value_first: {high_value_first}")
                            high_value = high_value_first
                            trade_possible_ce = True       
                    else:
                        print("Not enough data to determine last CE candle color.")
                else:
                    print("No CE chain data with volume information available.")
            else:
                print("BOT FOUND CE CHAIN")
            if not df_pe_chain.empty:
                df_pe_chain = df_pe_chain.sort_values("strike").reset_index(drop=True)
                df_pe_chain = df_pe_chain[df_pe_chain["strike"].isin(pe_strikes)]
                #print(df_pe_chain)
                file_exists = os.path.isfile(ce_csv_filename)
                # Add 'time' column with current complete date time with second
                df_pe_chain['time'] = datetime.now().strftime("%Y-%m-%d")
                df_pe_chain["TYPE"] ="PE"
                df_pe_chain.to_csv(ce_csv_filename, mode='a', index=False, header=not file_exists)
                if not df_pe_chain.empty and 'volume' in df_pe_chain.columns:
                    highest_vol_pe_df = df_pe_chain[df_pe_chain['volume'] == df_pe_chain['volume'].max()]
                    #print("PE(s) with highest volume:")
                    strike_point_pe = highest_vol_pe_df['strike'].iloc[0] if not highest_vol_pe_df.empty else None
                    high_vol = highest_vol_pe_df['volume'].iloc[0] if not highest_vol_pe_df.empty else None
                    trade_pe_security = df_pe[df_pe["STRIKE_PRICE"] == strike_point_pe]
                    pe_security = trade_pe_security["SECURITY_ID"].values[0] if not trade_pe_security.empty else None
                    user_data_pe = {
                        "securityId": str(pe_security),
                        "exchangeSegment": "NSE_FNO",
                        "instrument": "OPTIDX",
                        "interval": str(timeframe),
                        "fromDate": datetime.now().strftime("%Y-%m-%d"),
                        "toDate": datetime.now().strftime("%Y-%m-%d")
                   
                    }
                    #
                    intraday_response_pe = requests.post(url, headers=headers, json=user_data_pe)
                    #print(intraday_response_pe.json())
                    records_pe = intraday_response_pe.json() if intraday_response_pe.status_code == 200 else []
                    intraday_df_pe = pd.DataFrame(records_pe)
                    intraday_df_pe["timestamp"] = pd.to_datetime(intraday_df_pe["timestamp"], unit="s", utc=True).dt.tz_convert('Asia/Kolkata')
                    intraday_df_pe["time"] = pd.to_datetime(intraday_df_pe["timestamp"]).dt.time
                    target_time_pe = (datetime.now() - timedelta(minutes=1)).replace(second=0, microsecond=0)
                    target_time_pe_time = target_time_pe.time()  # .time() gets HH:MM:SS as time object
                    intraday_df_pe = intraday_df_pe[intraday_df_pe["time"] == target_time_pe_time]
                    print(intraday_df_pe)
                    if not intraday_df_pe.empty and {'open', 'close'}.issubset(intraday_df_pe.columns):
                        if len(intraday_df_pe) == 3:
                            last_candle = intraday_df_pe.iloc[1]
                        else:
                            last_candle = intraday_df_pe.iloc[0] 
                        open_price = last_candle['open']
                        close_price = last_candle['close']
                        candle_color_pe = "DOJI"
                        if close_price > open_price:
                            print("Last PE candle is GREEN")
                            candle_color_pe = "GREEN"
                        elif close_price < open_price:
                            print("Last PE candle is RED")
                            candle_color_pe = "RED"
                        else:
                            print("Last PE candle is DOJI")
                        #if candle_color_pe == "RED": 
                        if candle_color_spot == "Red":
                            if len(intraday_df_pe) == 3:
                                low_value_last = intraday_df_pe.iloc[2]['low']
                                low_value_first = intraday_df_pe.iloc[1]['low']
                                high_value_data = intraday_df_pe.iloc[1]['high']
                                #check break points 
                                last_candle_low_val = intraday_df_pe.iloc[1]['low']
                                last_candle_high_val = intraday_df_pe.iloc[1]['high']
                            elif len(intraday_df_pe) == 2:
                                low_value_last = intraday_df_pe.iloc[1]['low']
                                low_value_first = intraday_df_pe.iloc[0]['low']
                                high_value_data = intraday_df_pe.iloc[0]['high']
                                #check break points
                                last_candle_low_val = intraday_df_pe.iloc[0]['low']
                                last_candle_high_val = intraday_df_pe.iloc[0]['high']
                            else:
                                low_value_last = intraday_df_pe.iloc[0]['low']
                                low_value_first = intraday_df_pe.iloc[0]['low']
                                high_value_data = intraday_df_pe.iloc[0]['high']
                                #check break points
                                last_candle_low_val = intraday_df_pe.iloc[0]['low']
                                last_candle_high_val = intraday_df_pe.iloc[0]['high']
                            print("low_value_last:", low_value_last)
                            print("low_value_first:", low_value_first)
                            
                            low_value = high_value_data
                            pe_trade_possible = True
                    else:
                        print("Not enough data to determine last candle color.")
                else:
                    print("No PE chain data with volume information available.")
            else:
                print("NOT FOUND PE CHAIN")
            if pe_trade_possible:
                print("TRADE POSSIBLE IN PE AND PLACING ORDER====================")
                TICK_SIZE = 0.01
                low_value = (round(low_value / TICK_SIZE) * TICK_SIZE)
       
                order_url = "https://api.dhan.co/v2/orders"
                order_headers = {
                    "Content-Type": "application/json",
                    "access-token": access_token
                }
                # Make low_value a multiple of 0.05 and add 0.5
                low_value = (round(low_value / 0.05) * 0.05) + 0.05
         
                order_payload = {
                    "dhanClientId": "1106302772",
                    "correlationId": "123abcroopa15",
                    "transactionType": "BUY",
                    "exchangeSegment": "NSE_FNO",
                    "productType": "INTRADAY",
                    "orderType": "STOP_LOSS",
                    "validity": "DAY",
                    "securityId": str(pe_security),
                    "quantity": 65,
                    "price": float(low_value),
                    "triggerPrice": float(low_value-0.05)
                }
                entry_time_obj = datetime.now()
                try:
                    order_response = requests.post(order_url, headers=order_headers, json=order_payload)
                    order_response_json = order_response.json()
                    print(order_response_json)
                    order_id = order_response_json.get('orderId')
                    # Calculate target candle and target time
                    target_candle = exit_candle_count
                    target_time_obj = entry_time_obj + timedelta(minutes=int(timeframe)*int(exit_candle_count))
                    target_time_str = target_time_obj.strftime("%Y-%m-%d %H:%M:%S")
                    #make the exit time and exir price and pl
                    order_placed_data = {
                        "time": entry_time_obj.strftime("%Y-%m-%d %H:%M:%S"),
                        "transactionType": "BUY",
                        "symbol": str(trade_pe_security.iloc[0]['DISPLAY_NAME']) if not trade_pe_security.empty and 'DISPLAY_NAME' in trade_pe_security.columns else '-',
                        "securityId": str(pe_security),
                        "strike": strike_point_pe,
                        "orderId": str(order_id) if order_id else "-",
                        "status": "Requested" if order_id else order_response_json.get('message', "-"),
                        "price": round(float(low_value),2),
                        "quantity": 65,
                        "details": str(order_response_json),
                        "stoplossOrderId": "-",    # Placeholder for SL
                        "stoplossStatus": "-",     # Placeholder for SL
                        "stoplossPrice": "-",      # Placeholder for SL
                        "stoplossDetails": "-",    # Placeholder for SL
                        "targetCandle": str(target_candle),
                        "targetTime": target_time_str,
                        "lowBreakPoint": round(last_candle_low_val,2),
                        "highBreakPoint": round(last_candle_high_val,2),
                        "exitPrice": "-",          # Placeholder for exit price
                        "exitTime": "-",           # Placeholder for exit time
                        "exitSL": "-",             # Placeholder for exit stoploss, user can fill actual value later
                        "exitReason": "-" ,         # Placeholder for exit reason
                        "SPOT": float(spot),
                        "high vol":high_vol,
                        "VOL IN LOT":float(high_vol/65),
                    }            
                    if order_id:
                        get_order_url = f"https://api.dhan.co/v2/orders/{order_id}"
                        get_order_headers = {
                            "Content-Type": "application/json",
                            "access-token": access_token
                        }
                        try:
                            get_order_response = requests.get(get_order_url, headers=get_order_headers)
                            order_details = get_order_response.json()
                            details = order_details[0] if isinstance(order_details, list) and len(order_details) > 0 else order_details
                            order_status = details.get("orderStatus")
                            #include triggered here
                            if (order_status == "TRANSIT" or order_status == "TRADED"):
                                time.sleep(2)
                                get_order_response = requests.get(get_order_url, headers=get_order_headers)
                                order_details = get_order_response.json()
                                details = order_details[0] if isinstance(order_details, list) and len(order_details) > 0 else order_details
                                order_status = details.get("orderStatus")
                                price = details.get("price")
                                remaining_quantity = details.get("remainingQuantity")
                                quantity = details.get("quantity")
                                order_placed_data["status"] = order_status or "-"
                                order_placed_data["price"] = price
                                order_placed_data["quantity"] = quantity
                                order_placed_data["details"] = str(order_details)
                            else:
                                get_order_response = requests.get(get_order_url, headers=get_order_headers)
                                order_details = get_order_response.json()
                                details = order_details[0] if isinstance(order_details, list) and len(order_details) > 0 else order_details
                                order_status = details.get("orderStatus")
                                price = details.get("price")
                                remaining_quantity = details.get("remainingQuantity")
                                quantity = details.get("quantity")
                                order_placed_data["status"] = order_status or "-"
                                order_placed_data["price"] = price
                                order_placed_data["quantity"] = quantity
                                order_placed_data["details"] = str(order_details)
                            
                            poll_attempts = 0
                            max_attempts = 30
                            break_loop = False

                            print("INITIAL ORDER STATUS IS ==================================",order_status,remaining_quantity)
                
                            while ((order_status == "PENDING" or order_status == "CANCEL") and int(remaining_quantity) != 0 and datetime.now().second in range(1, 57)):
                                
                                print("MAX POL ATTENDED ==============================",poll_attempts,datetime.now().second)
                                print("WAITING ==================")
                                time.sleep(0.02)
                                if break_loop or datetime.now().second == 57:
                                    print("break while loop=============================================\n",datetime.now().second)
                                    break
                                else:
                           
                                    pass
                                try:
                                    user_data_get = {
                                        "securityId": str(pe_security),
                                        "exchangeSegment": "NSE_FNO",
                                        "instrument": "OPTIDX",
                                        "interval": str(timeframe),
                                        "fromDate": datetime.now().strftime("%Y-%m-%d"),
                                        "toDate": datetime.now().strftime("%Y-%m-%d")
                                    }
                                    #
                                    intraday_response_pe = requests.post(url, headers=headers, json=user_data_get)
                                    #print(intraday_response_pe.json())

                                    records_pe = intraday_response_pe.json() if intraday_response_pe.status_code == 200 else []
                                    intraday_df_pe = pd.DataFrame(records_pe)
                                    intraday_df_pe["timestamp"] = pd.to_datetime(intraday_df_pe["timestamp"], unit="s", utc=True).dt.tz_convert('Asia/Kolkata')
                                    # Get the low value from the last row of intraday_df_pe
                                    if not intraday_df_pe.empty and 'low' in intraday_df_pe.columns:
                                        low_value_test = intraday_df_pe.iloc[-1]['low']
                                        print(f"Low value from last row: {low_value_test} :{last_candle_low_val}")
                                        if float(low_value_test) < (last_candle_low_val):
                                            print("BREAK LOW VALUE SO CANCEL ORDER ============================================================\n")
                                            #break_loop = True
                                            break_loop = True
                                            
                                            #print("BREAK LOW VALUE SO CANCEL ORDER ============================================================\n")
                                            try:
                                                cancel_order_url = f"https://api.dhan.co/v2/orders/{order_id}"
                                                cancel_order_headers = {
                                                    "Content-Type": "application/json",
                                                    "access-token": access_token
                                                }
                                                cancel_order_response = requests.delete(cancel_order_url, headers=cancel_order_headers, timeout=10)
                                                try:
                                                    cancel_response_json = cancel_order_response.json()
                                                    order_placed_data["status"] = "CANCELLED"
                                                    order_status = "CANCELLED"
                                                    order_placed_data["details"] += "\nCancel JSON: " + str(cancel_response_json)
                                                    order_placed_data["exitReason"] = "Low Break"

                                                    break_loop = True
                                                    order_status = "CANCEL"
                                                    order_status_comp = "CANCEL"
                                                    #poll_attempts = max_attempts
                                                except Exception:
                                                    order_placed_data["details"] += "\nCancel: Could not decode JSON"
                                            except Exception as cancel_err:
                                                order_placed_data["details"] += "\nCancel error: " + str(cancel_err)
                                        else:
                                            get_order_response = requests.get(get_order_url, headers=get_order_headers)
                                            order_details = get_order_response.json()
                                            details = order_details[0] if isinstance(order_details, list) and len(order_details) > 0 else order_details
                                            order_status = details.get("orderStatus")
                                            price = details.get("price")
                                            remaining_quantity = details.get("remainingQuantity")
                                            quantity = details.get("quantity")
                                            order_placed_data["status"] = order_status or "-"
                                            order_placed_data["price"] = price
                                            order_placed_data["quantity"] = quantity
                                            order_placed_data["details"] = str(order_details)
                                    else:
                                        low_value = None
                                        print("Could not retrieve 'low' value from intraday_df_pe (empty or missing column).")
                                except Exception as poll_err:
                                    order_placed_data["status"] = f"Polling error: {poll_err}"
                                    break
                                poll_attempts += 1
                            while ((order_status or "").upper() == "TRIGGERED" or (order_status or "").upper() == "TRADED") and int(remaining_quantity!=0):
                                            get_order_response = requests.get(get_order_url, headers=get_order_headers)
                                            order_details = get_order_response.json()
                                            details = order_details[0] if isinstance(order_details, list) and len(order_details) > 0 else order_details
                                            order_status = details.get("orderStatus")
                                            price = details.get("price")
                                            remaining_quantity = details.get("remainingQuantity")
                                            quantity = details.get("quantity")
                                            order_placed_data["status"] = order_status or "-"
                                            order_placed_data["price"] = price
                                            order_placed_data["quantity"] = quantity
                                            order_placed_data["details"] = str(order_details)

                            if int(remaining_quantity) == 0 and ((order_status or "").upper() == "TRIGGERED" or (order_status or "").upper() == "COMPLETE" or (order_status or "").upper() == "TRADED"):
                                
                                print("filled and placing squer of leg ===============================",order_status)
                                prev_order_id = order_id
                                prev_security_id = str(pe_security)
                                entry_time_obj_sl = datetime.now()
                                prev_sl_exit = True
                                target_time_obj_sl = entry_time_obj_sl + timedelta(minutes=int(timeframe)*1)
                                sl_order_time = target_time_obj_sl.strftime("%Y-%m-%d %H:%M:%S")
                                order_placed_data["status"] = "COMPLETE"

                                print("======================================================================")
                                print("TRADE EXIT SL POSSIBLE NOW",remaining_quantity)
                                print("======================================================================")
                                try:
                                    time.sleep(0.30)
                                    trades_url = "https://api.dhan.co/v2/trades"
                                    trades_headers = {
                                        "Content-Type": "application/json",
                                        "access-token": access_token
                                    }
                                    trades_response = requests.get(trades_url, headers=trades_headers)
                                    trades_df = None
                                    try:
                                        trades_response_json = trades_response.json()
                                        if isinstance(trades_response_json, list):
                                            trades_df = pd.DataFrame(trades_response_json)
                                        else:
                                            print("Trades API did not return a list, got:", type(trades_response_json))
                                            trades_df = None

                                        trade_price_df = trades_df[
                                            (trades_df["securityId"].astype(str) == str(prev_security_id)) &
                                            (trades_df["orderId"].astype(str) == str(prev_order_id))
                                        ]

                                        print(trade_price_df,"trade_price book")
                                        if not trade_price_df.empty:
                                            traded_price = trade_price_df["tradedPrice"].iloc[0]
                                            print(traded_price)
                                            order_placed_data["price"] = trade_price_df["tradedPrice"].iloc[0] if not trade_price_df.empty else order_placed_data["price"]
                                            if orderbook and isinstance(orderbook[-1], dict):
                                                orderbook[-1]["price"] = traded_price
                                       
                                            stoploss_points_pe =  traded_price - (traded_price/stoploss_points)
                                            # Ensure stoploss_points_pe is rounded DOWN to the nearest multiple of TICK_SIZE
                                            TICK_SIZE = 0.05
                                            if TICK_SIZE > 0:
                                                stoploss_points_pe1 = (stoploss_points_pe // TICK_SIZE) * TICK_SIZE
                                            else:
                                                stoploss_points_pe1 = stoploss_points_pe
                                            # DH-906: Trigger Price should be greater than Price
                                            stoploss_price = float(stoploss_points_pe1)
                                            stoploss_trigger = stoploss_price + 0.05
                                            sl_order_payload = {
                                                "dhanClientId": "1106302772",
                                                "correlationId": "123abcroopa15",
                                                "transactionType": "SELL",
                                                "exchangeSegment": "NSE_FNO",
                                                "productType": "INTRADAY",
                                                "orderType": "STOP_LOSS",
                                                "validity": "DAY",
                                                "securityId": str(pe_security),
                                                "quantity": 65,
                                                "price": round(float(stoploss_price), 2),
                                                "triggerPrice": round(float(stoploss_trigger), 2),
                                            }
                                            
                                            print(sl_order_payload)
                                            order_url = "https://api.dhan.co/v2/orders"
                                            order_headers = {
                                                "Content-Type": "application/json",
                                                "access-token": access_token
                                            }
                                            #sl_order_response_json= {"ERROR":"ERROR"}
                                            sl_order_response = requests.post(order_url, headers=order_headers, json=sl_order_payload)
                                            sl_order_response_json = sl_order_response.json()
                                            print(sl_order_response_json)
                                            try:
                                                sl_order_id = sl_order_response_json.get('orderId')
                                                print(sl_order_id) 
                                                order_placed_data["stoplossOrderId"] = str(sl_order_id) if sl_order_id else "-"
                                                order_placed_data["stoplossStatus"] = "Requested" if sl_order_id else sl_order_response_json.get("message", "-")
                                                order_placed_data["stoplossPrice"] = round(float(stoploss_price), 2)
                                                order_placed_data["stoplossDetails"] = str(sl_order_response_json)
                                                prev_sl_exit = False

                                            except Exception as e:
                                                #print(sl_order_response_json)
                                                print("NOT ABLE TO PLACE SELL ORDER", e)
                                                order_placed_data["stoplossOrderId"] = "-"
                                                order_placed_data["stoplossStatus"] = f"Error placing SL: {e}"
                                                order_placed_data["stoplossPrice"] = float(stoploss_points_pe)
                                                order_placed_data["stoplossDetails"] = "-"    
                                        else:
                                            print(f"No trade found for securityId={prev_security_id}")
                                        
                                    except Exception as df_ex:
                                        trades_response_json = trades_response.json()
                                        print(f"Error occurred on line {df_ex.__traceback__.tb_lineno}: Could not convert trades response to dataframe: {df_ex}")
                                   
                                        trades_df = None

                                except Exception as trades_ex:
                                    print(f"Failed to fetch trades: {trades_ex}")
 
                            elif (str(order_status).upper() == "PENDING") or (str(order_status).upper() == "CANCEL"):
                                print("ORDER STATUS IS =======================================",order_status)
                                if datetime.now().second == 58 or order_status == "CANCEL" or order_status == "PENDING":
                                    try:
                                        cancel_order_url = f"https://api.dhan.co/v2/orders/{order_id}"
                                        cancel_order_headers = {
                                            "Content-Type": "application/json",
                                            "access-token": access_token
                                        }
                                        cancel_order_response = requests.delete(cancel_order_url, headers=cancel_order_headers, timeout=10)
                                        try:
                                            cancel_response_json = cancel_order_response.json()
                                            order_placed_data["status"] = "CANCELLED"
                                            order_status = "CANCELLED"
                                            order_placed_data["details"] += "\nCancel JSON: " + str(cancel_response_json)
                                            if order_status_comp == "CANCEL":
                                                order_placed_data["exitReason"] = "Low Break"
                                            else:
                                                order_placed_data["exitReason"] = "No high or no low break"
                                        except Exception:
                                            order_placed_data["details"] += "\nCancel: Could not decode JSON"
                                            #order_placed_data["exitReason"] = "No high or no low break"
                                    except Exception as cancel_err:
                                        order_placed_data["details"] += "\nCancel error: " + str(cancel_err)
                                else:
                                    print("no order too exit ======================",datetime.now().second)
                            else:
                                print("no order too exit ======================",datetime.now().second)
                        except Exception as e:
                            print(e, "NO ORDER RESPONSE ")
                    if order_placed_data:
                        orderbook.append(order_placed_data)
                except Exception as ex:
                    print(f"Order placement failed: {ex}")

            elif trade_possible_ce:
                print("TRADE POSSIBLE IN CE AND PLACING ORDER====================")
                high_value = (round(high_value / 0.01) * 0.01) + 0.05
         
                order_url = "https://api.dhan.co/v2/orders"
                order_headers = {
                    "Content-Type": "application/json",
                    "access-token": access_token
                }
                order_payload = {
                    "dhanClientId": "1106302772",
                    "correlationId": "123abcroopa15",
                    "transactionType": "BUY",
                    "exchangeSegment": "NSE_FNO",
                    "productType": "INTRADAY",
                    "orderType": "STOP_LOSS",
                    "validity": "DAY",
                    "securityId": str(ce_security),
                    "quantity": 65,
                    "price": float(high_value),
                    "triggerPrice": float(high_value-0.05)
                }
                entry_time_obj = datetime.now()
                try:
                    order_response = requests.post(order_url, headers=order_headers, json=order_payload)
                    order_response_json = order_response.json()
                    print(order_response_json)
                    order_id = order_response_json.get('orderId')
                    # Calculate target candle and target time
                    target_candle = exit_candle_count
                    target_time_obj = entry_time_obj + timedelta(minutes=int(timeframe)*int(exit_candle_count))
                    target_time_str = target_time_obj.strftime("%Y-%m-%d %H:%M:%S")
                    #make the exit time and exir price and pl
                    order_placed_data = {
                        "time": entry_time_obj.strftime("%Y-%m-%d %H:%M:%S"),
                        "transactionType": "BUY",
                        "symbol": str(trade_ce_security.iloc[0]['DISPLAY_NAME']) if not trade_ce_security.empty and 'DISPLAY_NAME' in trade_ce_security.columns else '-',
                        "securityId": str(ce_security),
                        "strike": strike_point_ce,
                        "orderId": str(order_id) if order_id else "-",
                        "status": "Requested" if order_id else order_response_json.get('message', "-"),
                        "price": round(float(high_value),2),
                        "quantity": 65,
                        "details": str(order_response_json),
                        "stoplossOrderId": "-",    # Placeholder for SL
                        "stoplossStatus": "-",     # Placeholder for SL
                        "stoplossPrice": "-",      # Placeholder for SL
                        "stoplossDetails": "-",    # Placeholder for SL
                        "targetCandle": str(target_candle),
                        "targetTime": target_time_str,
                        "lowBreakPoint": round(last_candle_low_val,2),
                        "highBreakPoint": round(last_candle_high_val,2),
                        "exitPrice": "-",          # Placeholder for exit price
                        "exitTime": "-",           # Placeholder for exit time
                        "exitSL": "-",             # Placeholder for exit stoploss, user can fill actual value later
                        "exitReason": "-"  ,        # Placeholder for exit reason
                        "SPOT": float(spot),
                        "high vol":high_vol,
                        "VOL IN LOT":float(high_vol/65),
                    }
                    #"high vol","VOL IN LOT"
      
                    if order_id:
                        get_order_url = f"https://api.dhan.co/v2/orders/{order_id}"
                        get_order_headers = {
                            "Content-Type": "application/json",
                            "access-token": access_token
                        }
                        try:
                            get_order_response = requests.get(get_order_url, headers=get_order_headers)
                            order_details = get_order_response.json()
                            details = order_details[0] if isinstance(order_details, list) and len(order_details) > 0 else order_details
                            order_status = details.get("orderStatus")
                            if (order_status == "TRANSIT" or order_status == "TRADED"):
                                time.sleep(2)
                                get_order_response = requests.get(get_order_url, headers=get_order_headers)
                                order_details = get_order_response.json()
                                details = order_details[0] if isinstance(order_details, list) and len(order_details) > 0 else order_details
                                order_status = details.get("orderStatus")
                                price = details.get("price")
                                remaining_quantity = details.get("remainingQuantity")
                                quantity = details.get("quantity")
                                order_placed_data["status"] = order_status or "-"
                                order_placed_data["price"] = price
                                order_placed_data["quantity"] = quantity
                                order_placed_data["details"] = str(order_details)
                            else:
                                get_order_response = requests.get(get_order_url, headers=get_order_headers)
                                order_details = get_order_response.json()
                                details = order_details[0] if isinstance(order_details, list) and len(order_details) > 0 else order_details
                                order_status = details.get("orderStatus")
                                price = details.get("price")
                                remaining_quantity = details.get("remainingQuantity")
                                quantity = details.get("quantity")
                                order_placed_data["status"] = order_status or "-"
                                order_placed_data["price"] = price
                                order_placed_data["quantity"] = quantity
                                order_placed_data["details"] = str(order_details)

                            poll_attempts = 0
                            max_attempts = 30
                            break_loop = False
                            print("INITIAL ORDER STATUS IS ==================================",order_status)

                            while ((order_status == "PENDING" or order_status == "CANCEL") and int(remaining_quantity) != 0 and datetime.now().second in range(1, 57)):
                                time.sleep(0.02)
                                print("MAX POL ATTENDED ==============================",poll_attempts,datetime.now().second)
                                if break_loop or datetime.now().second == 57:
                                    print("break while loop=============================================\n",datetime.now().second)
                                    break
                                else:
                                    pass
                                try:
                                    print("WAITING===================================================================")
                                    user_data_get = {
                                        "securityId": str(ce_security),
                                        "exchangeSegment": "NSE_FNO",
                                        "instrument": "OPTIDX",
                                        "interval": str(timeframe),
                                        "fromDate": datetime.now().strftime("%Y-%m-%d"),
                                        "toDate": datetime.now().strftime("%Y-%m-%d")
                                    }
                                    #
                                    intraday_response_ce = requests.post(url, headers=headers, json=user_data_get)
                                    records_ce = intraday_response_ce.json() if intraday_response_ce.status_code == 200 else []
                                    intraday_df_ce = pd.DataFrame(records_ce)
                                    intraday_df_ce["timestamp"] = pd.to_datetime(intraday_df_ce["timestamp"], unit="s", utc=True).dt.tz_convert('Asia/Kolkata')
                                    # Get the low value from the last row of intraday_df_pe
                                    if not intraday_df_ce.empty and 'low' in intraday_df_ce.columns:
                                        low_value_test = intraday_df_ce.iloc[-1]['low']
                                        print(f"Low value from last row: {low_value_test} : {last_candle_low_val}")
                                        if float(low_value_test) < float(last_candle_low_val):
                                            print("BREAK LOW VALUE SO CANCEL ORDER ============================================================\n")
                                            break_loop = True
                                            try:
                                                cancel_order_url = f"https://api.dhan.co/v2/orders/{order_id}"
                                                cancel_order_headers = {
                                                    "Content-Type": "application/json",
                                                    "access-token": access_token
                                                }
                                                cancel_order_response = requests.delete(cancel_order_url, headers=cancel_order_headers, timeout=10)
                                                try:
                                                    cancel_response_json = cancel_order_response.json()
                                                    order_placed_data["status"] = "CANCELLED"
                                                    order_status = "CANCELLED"
                                                    order_placed_data["exitReason"] = "Low Break"
                                                    order_placed_data["details"] += "\nCancel JSON: " + str(cancel_response_json)
                                                    break_loop = True
                                                    order_status = "CANCEL"
                                                    order_status_comp = "CANCEL"
                                                    #poll_attempts = max_attempts
                                                except Exception:
                                                    order_placed_data["details"] += "\nCancel: Could not decode JSON"
                                            except Exception as cancel_err:
                                                order_placed_data["details"] += "\nCancel error: " + str(cancel_err)
                                        else:
                                            get_order_response = requests.get(get_order_url, headers=get_order_headers)
                                            order_details = get_order_response.json()
                                            details = order_details[0] if isinstance(order_details, list) and len(order_details) > 0 else order_details
                                            order_status = details.get("orderStatus")
                                            price = details.get("price")
                                            remaining_quantity = details.get("remainingQuantity")
                                            quantity = details.get("quantity")
                                            order_placed_data["status"] = order_status or "-"
                                            order_placed_data["price"] = price
                                            order_placed_data["quantity"] = quantity
                                            order_placed_data["details"] = str(order_details)

                                    else:
                                        low_value = None
                                        print("Could not retrieve 'low' value from intraday_df_pe (empty or missing column).")
                                    
                                except Exception as poll_err:
                                    order_placed_data["status"] = f"Polling error: {poll_err}"
                                    break
                                poll_attempts += 1
                            

                            while ((order_status or "").upper() == "TRIGGERED" or (order_status or "").upper() == "TRADED") and int(remaining_quantity!=0):
                                            get_order_response = requests.get(get_order_url, headers=get_order_headers)
                                            order_details = get_order_response.json()
                                            details = order_details[0] if isinstance(order_details, list) and len(order_details) > 0 else order_details
                                            order_status = details.get("orderStatus")
                                            price = details.get("price")
                                            remaining_quantity = details.get("remainingQuantity")
                                            quantity = details.get("quantity")
                                            order_placed_data["status"] = order_status or "-"
                                            order_placed_data["price"] = price
                                            order_placed_data["quantity"] = quantity
                                            order_placed_data["details"] = str(order_details)
                            #if int(remaining_quantity) == 0 or (order_status or "").upper() == "TRIGGERED":
                            if int(remaining_quantity) == 0 and ((order_status or "").upper() == "TRIGGERED" or (order_status or "").upper() == "COMPLETE" or (order_status or "").upper() == "TRADED"):
                                
                                print("filled and placing squer of leg ===============================",order_status)
                                prev_order_id = order_id
                                prev_security_id = str(ce_security)
                                entry_time_obj_sl = datetime.now()
                                prev_sl_exit = True
                                target_time_obj_sl = entry_time_obj_sl + timedelta(minutes=int(timeframe)*1)
                                sl_order_time = target_time_obj_sl.strftime("%Y-%m-%d %H:%M:%S")
                                order_placed_data["status"] = "COMPLETE"
                                print("======================================================================")
                                print("TRADE EXIT SL POSSIBLE NOW CE ",remaining_quantity)
                                print("======================================================================")
                                try:
                                    time.sleep(0.02)
                                    trades_url = "https://api.dhan.co/v2/trades"
                                    trades_headers = {
                                        "Content-Type": "application/json",
                                        "access-token": access_token
                                    }
                                    trades_response = requests.get(trades_url, headers=trades_headers)
                                    #print(trades_response.json())
                                    trades_df = None
                                    try:
                                        trades_response_json = trades_response.json()
                                        if isinstance(trades_response_json, list):
                                            trades_df = pd.DataFrame(trades_response_json)
                                        else:
                                            print("Trades API did not return a list, got:", type(trades_response_json))
                                            trades_df = None
                                        trade_price_df = trades_df[
                                            (trades_df["securityId"].astype(str) == str(prev_security_id)) &
                                            (trades_df["orderId"].astype(str) == str(prev_order_id))
                                        ]
                                   
                                        print(trade_price_df,"trade_price book")
                                        if not trade_price_df.empty:
                                            traded_price = trade_price_df["tradedPrice"].iloc[0]
                                            print(traded_price)
                                            order_placed_data["price"] = trade_price_df["tradedPrice"].iloc[0] if not trade_price_df.empty else order_placed_data["price"]
                                            if orderbook and isinstance(orderbook[-1], dict):
                                                orderbook[-1]["price"] = traded_price
                                       
                                            stoploss_points_pe =  traded_price - (traded_price/stoploss_points)
                                            # Ensure stoploss_points_pe is rounded DOWN to the nearest multiple of TICK_SIZE
                                            TICK_SIZE = 0.05
                                            if TICK_SIZE > 0:
                                                stoploss_points_pe1 = (stoploss_points_pe // TICK_SIZE) * TICK_SIZE
                                            else:
                                                stoploss_points_pe1 = stoploss_points_pe
                                            stoploss_price = float(stoploss_points_pe1)
                                            stoploss_trigger = stoploss_price + 0.05
                                            
                                            sl_order_payload = {
                                                "dhanClientId": "1106302772",
                                                "correlationId": "123abcroopa15",
                                                "transactionType": "SELL",
                                                "exchangeSegment": "NSE_FNO",
                                                "productType": "INTRADAY",
                                                "orderType": "STOP_LOSS",
                                                "validity": "DAY",
                                                "securityId": str(ce_security),
                                                "quantity": 65,
                                                "price": round(float(stoploss_price), 2),
                                                "triggerPrice": round(float(stoploss_trigger), 2),
                                            }
                                            print(sl_order_payload)
                                            order_url = "https://api.dhan.co/v2/orders"
                                            order_headers = {
                                                "Content-Type": "application/json",
                                                "access-token": access_token
                                            }
                                            #sl_order_response_json= {"ERROR":"ERROR"}
                                            sl_order_response = requests.post(order_url, headers=order_headers, json=sl_order_payload)
                                            sl_order_response_json = sl_order_response.json()
                                            print(sl_order_response_json)
                                            try:
                                                sl_order_id = sl_order_response_json.get('orderId')
                                                print(sl_order_id) 
                                                order_placed_data["stoplossOrderId"] = str(sl_order_id) if sl_order_id else "-"
                                                order_placed_data["stoplossStatus"] = "Requested" if sl_order_id else sl_order_response_json.get("message", "-")
                                                order_placed_data["stoplossPrice"] = round(float(stoploss_price), 2)
                                                order_placed_data["stoplossDetails"] = str(sl_order_response_json)
                                                prev_sl_exit = False

                                            except Exception as e:
                                                #print(sl_order_response_json)
                                                print("NOT ABLE TO PLACE SELL ORDER", e)
                                                order_placed_data["stoplossOrderId"] = "-"
                                                order_placed_data["stoplossStatus"] = f"Error placing SL: {e}"
                                                order_placed_data["stoplossPrice"] = float(stoploss_points_pe)
                                                order_placed_data["stoplossDetails"] = "-"    
                                        else:
                                            print(f"No trade found for securityId={prev_security_id}")
                                        
                                    except Exception as df_ex:
                                        trades_response_json = trades_response.json()
                                        print(f"Error occurred on line {df_ex.__traceback__.tb_lineno}: Could not convert trades response to dataframe: {df_ex}")
                                   
                                        trades_df = None
                                   
                                    #print("Trades API response:", trades_response_json)
                                except Exception as trades_ex:
                                    print(f"Failed to fetch trades: {trades_ex}")


                            elif (str(order_status).upper() == "PENDING") or (str(order_status).upper() == "CANCEL"):
                                print("ORDER STATUS IS =======================================",order_status)
                       
                                if datetime.now().second == 58 or order_status == "CANCEL" or order_status == "PENDING":
                           
                                    try:
                                        cancel_order_url = f"https://api.dhan.co/v2/orders/{order_id}"
                                        cancel_order_headers = {
                                            "Content-Type": "application/json",
                                            "access-token": access_token
                                        }
                                        cancel_order_response = requests.delete(cancel_order_url, headers=cancel_order_headers, timeout=10)
                                        try:
                                            cancel_response_json = cancel_order_response.json()
                                            order_placed_data["status"] = "CANCELLED"
                                            order_status = "CANCELLED"
                                            order_placed_data["details"] += "\nCancel JSON: " + str(cancel_response_json)
                                            #order_placed_data["exitReason"] = "No high or no low break"
                                            if order_status_comp == "CANCEL":
                                                order_placed_data["exitReason"] = "Low Break"
                                            else:
                                                order_placed_data["exitReason"] = "No high or no low break"
                                        except Exception:
                                            order_placed_data["details"] += "\nCancel: Could not decode JSON"
                                            #order_placed_data["exitReason"] = "No high or no low break"
                                    except Exception as cancel_err:
                                        order_placed_data["details"] += "\nCancel error: " + str(cancel_err)
                                else:
                                    print("no order too exit ======================",datetime.now().second)
                            else:
                                print("no order too exit ======================",datetime.now().second)
                        except Exception as e:
                            print(e, "NO ORDER RESPONSE")
                    if order_placed_data:
                        orderbook.append(order_placed_data)
                except Exception as ex:
                    print(f"Order placement failed: {ex}")
        else:
            if current_second in (3, 4, 5, 57, 58, 59) and (datetime.now().hour < 15 or (datetime.now().hour == 15 and datetime.now().minute < 15)):
                exit_all = True
       
                orderbook_detail = pd.DataFrame(orderbook)
                if not orderbook_detail.empty:
                    orderbook_data_exit = orderbook_detail[
                        (orderbook_detail["stoplossOrderId"].astype(str).str.isdigit()) & 
                        (orderbook_detail["status"].str.upper() != "CANCELLED")
                    ].copy()
                    #print(orderbook_data_exit)
                    # Only proceed if we have a targetTime column (means we've got timed exits mapped)
                    if "targetTime" in orderbook_data_exit.columns and not orderbook_data_exit.empty:
                        now = datetime.now()

                        def same_hour_minute(target_time_str):
                            try:
                                # Try to handle full datetime strings like '2026-07-08 09:53:03'
                                # as well as just 'HH:MM:SS' or 'HH:MM'
                                possible_formats = ("%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H:%M", "%H:%M:%S", "%H:%M")
                                t = None
                                for fmt in possible_formats:
                                    try:
                                        dt = datetime.strptime(str(target_time_str), fmt)
                                        t = dt.time() if ' ' in fmt else dt  # Datetime with date - .time(), just time - itself
                                        break
                                    except ValueError:
                                        continue
                                if t is None:
                                    return False

                                # Use only the hour and minute part
                                return t.hour == now.hour and t.minute == now.minute
                            except Exception:
                                return False

                        filtered_exit_data = orderbook_data_exit[
                            orderbook_data_exit["targetTime"].apply(same_hour_minute)
                        ]
                        #print(filtered_exit_data)
             
                        if not filtered_exit_data.empty:
                            order_id_exit = filtered_exit_data["stoplossOrderId"].iloc[0]
                            print("EXIT LEG ORDER ID IS=======================",order_id_exit)
                            security_id_exit = filtered_exit_data["securityId"].iloc[0]
                            #print(filtered_exit_data)
                            get_order_url = f"https://api.dhan.co/v2/orders/{order_id_exit}"
                            get_order_headers = {
                                "Content-Type": "application/json",
                                "access-token": access_token
                            }
                            try:
                                get_order_response = requests.get(get_order_url, headers=get_order_headers)
                                order_details = get_order_response.json()
                                print(order_details,"exit leg order details=========================================")
                                details = order_details[0] if isinstance(order_details, list) and len(order_details) > 0 else order_details
                                order_status = details.get("orderStatus")
                                remaining_quantity = details.get("remainingQuantity")
                                if order_status == "PENDING" and int(remaining_quantity) != 0:
                                    try:
                                        cancel_order_url = f"https://api.dhan.co/v2/orders/{order_id_exit}"
                                        cancel_order_headers = {
                                            "Content-Type": "application/json",
                                            "access-token": access_token
                                        }
                                        cancel_order_response = requests.delete(cancel_order_url, headers=cancel_order_headers, timeout=10)
                                        try:
                                            cancel_response_json = cancel_order_response.json()
                                            print("Order cancelled")
                                            print("Placing new exit order")
                                            order_url = "https://api.dhan.co/v2/orders"
                                            order_headers = {
                                                "Content-Type": "application/json",
                                                "access-token": access_token
                                            }
                                            order_payload = {
                                                "dhanClientId": "1106302772",
                                                "correlationId": "123abcroopa15",
                                                "transactionType": "SELL",
                                                "exchangeSegment": "NSE_FNO",
                                                "productType": "INTRADAY",
                                                "orderType": "MARKET",
                                                "validity": "DAY",
                                                "securityId": str(security_id_exit),
                                                "quantity": 65,
                                                "price": ""
                                                # No "price" key for market order
                                            }
                                            try:
                                                order_response = requests.post(order_url, headers=order_headers, json=order_payload)
                                                order_response_json = order_response.json()
                                                print(order_response_json)
                                                new_order_id = order_response_json.get('orderId')
                                                print("Placed order exit leg, new order ID:", new_order_id)
                                                #print("Already exit Done")
                                                trades_url = "https://api.dhan.co/v2/trades"
                                                trades_headers = {
                                                    "Content-Type": "application/json",
                                                    "access-token": access_token
                                                }
                                                trades_response = requests.get(trades_url, headers=trades_headers)
                                                #print(trades_response.json())
                                                trades_df = None
                                                try:
                                                    trades_response_json = trades_response.json()
                                                    if isinstance(trades_response_json, list):
                                                        trades_df = pd.DataFrame(trades_response_json)
                                                    else:
                                                        print("Trades API did not return a list, got:", type(trades_response_json))
                                                        trades_df = None
                                                    trade_price_df = trades_df[
                                                        (trades_df["securityId"].astype(str) == str(security_id_exit)) &
                                                        (trades_df["orderId"].astype(str) == str(new_order_id))
                                                    ]
                                            
                                                    print(trade_price_df,"trade_price book")
                                                    if not trade_price_df.empty:
                                                        traded_price = trade_price_df["tradedPrice"].iloc[0]
                                                        print(traded_price)
                                                        
                                                        found_stoploss_id = False
                                                        for idx, ob in enumerate(orderbook):
                                                            print(f"Checking orderbook index {idx}: stoplossOrderId={ob.get('stoplossOrderId')} vs security_id_exit={order_id_exit}")
                                                            # Compare both as strings with whitespace stripped for extra robustness
                                                            stoploss_id_ob = str(ob.get("stoplossOrderId", "")).strip()
                                                            sec_id_exit_str = str(order_id_exit).strip()
                                                            if stoploss_id_ob == sec_id_exit_str:
                                                                found_stoploss_id = True
                                                                exit_price = trade_price_df["tradedPrice"].iloc[0] if not trade_price_df.empty else ob.get("exitPrice")
                                                                orderbook[idx]["exitPrice"] = exit_price
                                                                orderbook[idx]["exitTime"] = datetime.now().strftime("%Y-%m-%d")
                                                                try:
                                                                    orderbook[idx]["exitSL"] = round(float(exit_price) - float(ob.get("price", 0)),2)
                                                                except Exception:
                                                                    orderbook[idx]["exitSL"] = "-"
                                                                orderbook[idx]["exitReason"] = "TARGET CANDLE HIT"
                                                        if not found_stoploss_id:
                                                            # Print detailed info for debug
                                                            print("NOT FOUND THE EXIT STOPLOSS ID")
                                                            print("security_id_exit:", security_id_exit, "orderbook stoplossOrderId list:", [ob.get("stoplossOrderId") for ob in orderbook])
                                                except Exception as exit_err:
                                                    print("ERROR EXIT:---------------------",exit_err)
                                            except Exception as e:
                                                print("Failed to place new exit order:", e)
                                        except Exception as cancel_json_err:
                                            print("Failed to parse cancel response:", cancel_json_err)
                                    except Exception as cancel_err:
                                        print("Error cancelling order:", cancel_err)
                                else:
                                    if order_status == "COMPLETE" or int(remaining_quantity) == 0:
                                        print("Already exit Done")
                                        trades_url = "https://api.dhan.co/v2/trades"
                                        trades_headers = {
                                            "Content-Type": "application/json",
                                            "access-token": access_token
                                        }
                                        trades_response = requests.get(trades_url, headers=trades_headers)
                                        print(trades_response.json())
                                        trades_df = None
                                        try:
                                            trades_response_json = trades_response.json()
                                            if isinstance(trades_response_json, list):
                                                trades_df = pd.DataFrame(trades_response_json)
                                            else:
                                                print("Trades API did not return a list, got:", type(trades_response_json))
                                                trades_df = None
                                            trade_price_df = trades_df[
                                                (trades_df["securityId"].astype(str) == str(security_id_exit)) &
                                                (trades_df["orderId"].astype(str) == str(order_id_exit))
                                            ]
                                    
                                            print(trade_price_df,"trade_price book")
                                            if not trade_price_df.empty:
                                                        traded_price = trade_price_df["tradedPrice"].iloc[0]
                                                        print(traded_price)
                                                        found_stoploss_id = False
                                                        
                                                        for idx, ob in enumerate(orderbook):
                                                            print(f"Checking orderbook index {idx}: stoplossOrderId={ob.get('stoplossOrderId')} vs security_id_exit={order_id_exit}")
                                                            # Compare both as strings with whitespace stripped for extra robustness
                                                            stoploss_id_ob = str(ob.get("stoplossOrderId", "")).strip()
                                                            sec_id_exit_str = str(order_id_exit).strip()
                                                            if stoploss_id_ob == sec_id_exit_str:
                                                                found_stoploss_id = True
                                                                exit_price = trade_price_df["tradedPrice"].iloc[0] if not trade_price_df.empty else ob.get("exitPrice")
                                                                orderbook[idx]["exitPrice"] = exit_price
                                                                orderbook[idx]["exitTime"] = datetime.now().strftime("%Y-%m-%d")
                                                                try:
                                                                    orderbook[idx]["exitSL"] = round(float(exit_price) - float(ob.get("price", 0)),2)
                                                                except Exception:
                                                                    orderbook[idx]["exitSL"] = "-"
                                                                orderbook[idx]["exitReason"] = "STOPLOSS HIT"
                                                        if not found_stoploss_id:
                                                            # Print detailed info for debug
                                                            print("NOT FOUND THE EXIT STOPLOSS ID")
                                                            print("security_id_exit:", security_id_exit, "orderbook stoplossOrderId list:", [ob.get("stoplossOrderId") for ob in orderbook])
                                        
                                                #order_placed_data["price"] = trade_price_df["tradedPrice"].iloc[0] if not trade_price_df.empty else order_placed_data["price"]
                                        except Exception as exit_err:
                                            print("ERROR EXIT:---------------------",exit_err)
                                    else:
                                        print("ORDER CANCELLED")
                            except Exception as e:
                                print("Error in exit order workflow:", e)
                        else:
                            pass
                    else:
                        pass
                else:
                    orderbook_data_exit = pd.DataFrame()
                    security_ids_to_check = []
            else:
                if datetime.now().hour == 15 and datetime.now().minute > 15 and exit_all:
                    exit_all = False
                    import requests

                    try:
                        headers = {
                            "Accept": "application/json",
                            "access-token": access_token
                        }
                        response = requests.delete("https://api.dhan.co/v2/positions", headers=headers)
                        if response.status_code == 200:
                            print("All open positions exited successfully.")
                        else:
                            print(f"Failed to exit all positions. Status Code: {response.status_code}, Response: {response.text}")
                    except Exception as e:
                        print(f"Exception occurred while trying to exit all open positions: {e}")
             
                    print("EXIT ALL OPEN POSITIONS")
                else:
                    pass
          
    except Exception as e:
        print(e)

if __name__ == "__main__":
    print("Welcome to Nifty Auto-Order Bot (Dhan API)")
    access_token, timeframe, stoploss_points, exit_candle_count = get_user_inputs()
    already_opened_oc = False
    launch_orderbook_frontend(open_browser=True)
    while True:
        live_data(access_token, timeframe, stoploss_points, exit_candle_count, open_browser_on_output=(not already_opened_oc))
        if not already_opened_oc:
            already_opened_oc = True
