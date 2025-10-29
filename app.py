from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = "secret-key"  # session 用

@app.route('/', methods=['GET', 'POST'])
def index():
    output_message = None
    results = []

    if request.method == 'POST':
        grade = int(request.form.get('grade'))
        classroom = int(request.form.get('classroom'))
        number2 = int(request.form.get('number2'))

        # キーを「学年-クラス」で作成
        key = f"{grade}-{classroom}"

        if key not in session:
            session[key] = []

        results = session[key]

        all_numbers = list(range(1, number2 + 1))
        remaining = list(set(all_numbers) - set(results))

        if not remaining:
            output_message = f"{grade}年{classroom}組は全て抽選済みです！"
        else:
            selected = random.choice(remaining)
            results.append(selected)
            session[key] = results
            session.modified = True

            output_message = f"結果: {grade}年{classroom}組 {selected}番"

    # 履歴一覧（全学年クラス表示）
    history = {k: v for k, v in session.items() if k != "_flashes"}

    return render_template("index.html",
                           output_message=output_message,
                           history=history)

@app.route('/reset_all')
def reset_all():
    session.clear()
    return render_template("index.html", output_message="全履歴を削除しました！")

if __name__ == '__main__':
    app.run(debug=True)
