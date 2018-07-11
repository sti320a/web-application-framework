#! python3

import os, sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '\\..\\')
import sendEmailService as se

print("Checking sending Email Mock...")
assert(se.sendEmailMock("xxx@gmail.com", "モックメールサンプル", "モックメール送信のテスト"))


print("Finish All Test.")