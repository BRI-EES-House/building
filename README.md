# building

<a href='https://bri-ees-building-spec.readthedocs.io/ja/latest/?badge=latest'>
    <img src='https://readthedocs.org/projects/bri-ees-building-spec/badge/?version=latest' alt='Documentation Status' />
</a>

## 公開用URL（HTML）

https://bri-ees-building-spec.readthedocs.io/ja/latest/


## 更新手順
Visual Studio Code (https://code.visualstudio.com/) とGit (https://gitforwindows.org/)をダウンロード.

○デスクトップでもピクチャでもビデオでも好きなフォルダ(以下、任意のフォルダ)で右クリックして、Git Bash Hereをクリック
○gitのユーザー名・メールアドレスの設定(これをしないと後述のVS Codeでコミットができない)

Git Bash画面上で、それぞれ
$ git config --global user.name "自分のユーザー名"
$ git config --global user.email "自分のメールアドレス"
を入力して、設定、Git Bashはまだ閉じない。

○リモートリポジトリの設定(これをしないと後述のVS CodeでPushができない)
Git Bash Here画面上で、
$ git remote add origin http://xxxxxx.xxx/xxxx.git(自分のGitHub URL)
を入力する。

○ローカルへのクローン
https://github.com/BRI-EES-House/building.gitにアクセスし、Forkボタンを押すと、自分のアカウントページにFork（コピー）したリポジトリが表示される。
これを自分のパソコンにクローン（コピー）する。
リポジトリの「Code」ボタンに表示されているURLをコピーし、
Git Bash Here画面上で、
$ git init
$ git clone コピーしたURL
を入力する。
なお、自分のアカウントにForkした後に本体のリポジトリが更新されており、
自分のアカウントのリポジトリが最新版でない場合は、ローカルの任意のフォルダにコピーしたリポジトリに最新版を反映させ、自分のアカウントのリポジトリも最新版にしておく。
ローカルフォルダを右クリックして、Git Bash Hereをクリックし、
マージ先のブランチをチェックアウトし、本体のブランチをプルし、自分のアカウントにプッシュする。
git checkout master
git pull 本体のURL master
git push origin master

VS codeによる更新(※以下は、VSCodeで実行。)
○フォルダを右クリックして、Codeで開くをクリック
○修正するまえに、ブランチを切る
最初はmasterブランチになっているはずなので、新しいブランチを作成する。ブランチ名は何でもいい
(適宜、ブランチは削除等して整理する。ただし、本体のpull request承認前に消すと、pull requestも消えるので、承認されるまでは残しておくこと！)
○ブランチが切り替わっていることを確かめたうえで、内容を修正
○修正が終われば、ファイルタブの保存をクリック
○左側のソース管理タブから、変更をステージングにする
○コミットメッセージを入れてコミットする
○これで変更が確定。今度はこれを、自分のgithubのリポジトリにアップロードする。
ソース管理タブの「…」をクリックして、その中のプッシュ先…をクリック、その次にoriginにプッシュしてしばらく待てば、VS codeでの作業は終了。
