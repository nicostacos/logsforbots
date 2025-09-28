import socketserver
import requests

DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1421950339619356733/iMU1_66BgY9tfbYBanWXOOykrDCK9cKEBskOZJSfktjivOML9_Gn57TRZTs3eilGehM1"

class SyslogHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request[0].strip().decode("utf-8")
        print("Log received:", data)

        # Send ALL logs to Discord
        payload = {"content": f"📝 Render Log: {data}"}
        try:
            requests.post(DISCORD_WEBHOOK, json=payload)
        except Exception as e:
            print("Failed to send to Discord:", e)

if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 514  # safer than 514 on Windows
    with socketserver.UDPServer((HOST, PORT), SyslogHandler) as server:
        print("Syslog server listening on port", PORT)
        server.serve_forever()
