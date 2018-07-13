#! python3

DB_FILE_NAME = "testUserDb"


EMAIL_SUBJECT_SIGNUP_CONFIRM = "本登録を完了しましょう。"
EMAIL_BODY_SIGNUP_CONFIRM = """
{}様 \n 
本サービスにご登録頂きありがとうございます。\n 
以下のリンクから本登録を完了しましょう。\n 
https://sample.com/signup?p={}\n \n 
今後とも当サービスをよろしくお願いいたします。
"""