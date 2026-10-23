from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>AWS DevOps Project</title>

        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }

            body {
                font-family: Arial, sans-serif;
                min-height: 100vh;
                background: linear-gradient(135deg, #0f172a, #1e1b4b, #312e81);
                color: #f8fafc;
                display: flex;
                justify-content: center;
                align-items: center;
                padding: 25px;
            }

            .container {
                max-width: 850px;
                width: 100%;
                text-align: center;
            }

            .badge {
                display: inline-block;
                padding: 9px 18px;
                border: 1px solid #334155;
                border-radius: 30px;
                color: #67e8f9;
                background: rgba(15, 23, 42, 0.7);
                font-size: 14px;
                margin-bottom: 25px;
            }

            h1 {
                font-size: clamp(36px, 7vw, 58px);
                margin-bottom: 20px;
                line-height: 1.15;
            }

            h1 span {
                background: linear-gradient(90deg, #38bdf8, #a78bfa);
                -webkit-background-clip: text;
                background-clip: text;
                color: transparent;
            }

            .description {
                color: #cbd5e1;
                font-size: 18px;
                line-height: 1.8;
                margin: 0 auto 35px;
                max-width: 650px;
            }

            .cards {
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 16px;
                margin-bottom: 28px;
            }

            .card {
                background: rgba(255, 255, 255, 0.06);
                border: 1px solid rgba(255, 255, 255, 0.12);
                border-radius: 16px;
                padding: 25px 12px;
                transition: transform 0.2s, background 0.2s;
            }

            .card:hover {
                transform: translateY(-5px);
                background: rgba(255, 255, 255, 0.11);
            }

            .icon {
                font-size: 30px;
                margin-bottom: 14px;
            }

            .card h2 {
                font-size: 17px;
                margin-bottom: 9px;
            }

            .card p {
                font-size: 13px;
                color: #cbd5e1;
                line-height: 1.6;
            }

            .status {
                display: inline-flex;
                align-items: center;
                gap: 9px;
                background: rgba(22, 163, 74, 0.15);
                border: 1px solid rgba(74, 222, 128, 0.3);
                border-radius: 30px;
                padding: 12px 20px;
                color: #86efac;
                font-size: 14px;
            }

            .dot {
                height: 9px;
                width: 9px;
                border-radius: 50%;
                background: #4ade80;
                box-shadow: 0 0 10px #4ade80;
            }

            footer {
                color: #94a3b8;
                margin-top: 35px;
                font-size: 13px;
                line-height: 1.8;
            }

            @media (max-width: 600px) {
                .cards {
                    grid-template-columns: 1fr;
                }

                .description {
                    font-size: 16px;
                }

                .card {
                    padding: 20px;
                }
            }
        </style>
    </head>

    <body>
        <main class="container">
            <div class="badge">☁️ AWS CLOUD PROJECT</div>

            <h1>Building the Future with <span>DevOps</span></h1>

            <p class="description">
                My application is running successfully!
                This project demonstrates automated application delivery
                using modern DevOps tools and cloud infrastructure.
            </p>

            <section class="cards">
                <div class="card">
                    <div class="icon">🐳</div>
                    <h2>Docker</h2>
                    <p>Containerization and consistent application packaging</p>
                </div>

                <div class="card">
                    <div class="icon">⚙️</div>
                    <h2>Jenkins</h2>
                    <p>Continuous integration and automated delivery</p>
                </div>

                <div class="card">
                    <div class="icon">☸️</div>
                    <h2>Kubernetes</h2>
                    <p>Container orchestration learning and deployment</p>
                </div>
            </section>

            <div class="status">
                <span class="dot"></span>
                Application Status: Healthy
            </div>

            <footer>
                AWS DevOps End-to-End Project<br>
                Built with Flask · Docker · Jenkins · AWS
            </footer>
        </main>
    </body>
    </html>
    """


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": "aws-devops-app"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
