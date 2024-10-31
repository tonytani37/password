## ppapでファイルをメールに添付して送付したいときにzipのパスワードを作成するスクリプト

### 同じようなヤツをjavascriptで作ってみたので（copilotのコード丸コピーですが）、コイツをブラウザで開くだけでパスワードが作れます。またリロードしない限り、作成済みのパスワードが画面に表示され続けますよ。

~~~
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>パスワード生成器</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
    <link rel="stylesheet" href="styles.css">
    <style>
        .custom-container {
            max-width: 800px; 
            margin: 0 auto; /* 中央揃え */
        }
        .custom-jumbotron {
            max-width: 800px; 
            margin: 0 auto; /* 中央揃え */
        }
    </style>
</head>
<body>
    <div class="jumbotron custom-jumbotron jumbotron-fluid">
        <div class="container">
          <h1 class="display-5">パスワードをつくる</h1>
          <p class="lead">[つくる]ボタンをクリックするとパスワードが作成されます
          <br>
          パスワードをクリックするとコピーできます</p>
        </div>
    </div>
    <div class="container-sm custom-container">
        <label for="length">パスワードの長さ (8-20):</label>
        <input type="number" id="length" name="length" min="8" max="20" value="12">
        <button onclick="generatePassword()"  class="btn btn-primary">つくる</button>
        <br><br>
        <div class="alert alert-primary" role="alert">
            <p id="password" onclick="copyPassword(this)" class="password-item"></p>
        </div>
        <div class="alert alert-success" role="alert">
            <p id="copy-message" class="copy-message"></p>
        </div>
        <div class="history">
            <p class="lead">これまでつくったもの（上から新しい順）</p>
             注意）リロードすると履歴は消えます
            <div class="alert alert-dark" role="alert">
                <ul id="history"></ul>
            </div>
        </div>

    </div>
    <script>
        function generatePassword() {
            const length = document.getElementById('length').value;
            const charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
            let password = "";
            for (let i = 0; i < length; i++) {
                const randomIndex = Math.floor(Math.random() * charset.length);
                password += charset[randomIndex];
            }
            const passwordElement = document.getElementById('password');
            passwordElement.textContent = password;
            addToHistory(password);
            document.getElementById('copy-message').textContent = ""; // Clear copy message
        }

        function addToHistory(password) {
            const historyList = document.getElementById('history');
            const listItem = document.createElement('li');
            listItem.textContent = password;
            listItem.className = 'password-item';
            listItem.onclick = function() { copyPassword(listItem); };
            historyList.insertBefore(listItem, historyList.firstChild); // 最新のパスワードを上に追加
        }

        function copyPassword(element) {
            const password = element.textContent;
            navigator.clipboard.writeText(password).then(() => {
                document.getElementById('copy-message').textContent = password+" がクリップボードにコピーされました！";
            }).catch(err => {
                console.error('Failed to copy: ', err);
            });
        }
    </script>
</body>
</html>
~~~
