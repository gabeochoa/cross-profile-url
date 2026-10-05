import unittest, unittest.mock as m, oip
class T(unittest.TestCase):
  def test_injection_url_is_one_argv_element_no_shell(self):
    evil='https://x.test/"; echo PWNED; echo "'
    with m.patch.object(oip.subprocess,"run") as run: oip.open_url(evil)
    args,kw=run.call_args; self.assertFalse(kw.get("shell")); argv=args[0]
    self.assertEqual(argv[-1],evil); self.assertEqual(len(argv),3)
  def test_rejects_non_http_and_quote_breakout_schemes(self):
    for u in ["javascript:alert(1)","file:///etc/passwd","https://","ftp://x/"]: self.assertRaises(ValueError,oip.build_argv,u)
  def test_source_has_no_shell(self): self.assertNotIn("shell=True",open("oip.py").read())
if __name__=="__main__": unittest.main()
class ProtocolT(unittest.TestCase):
  def test_no_stdout_print_and_bad_input_gets_response(self):
    self.assertNotRegex(open("oip.py").read(), r"(?m)^\s*print\((?!.*sys\.stderr)")
    import io,struct,json
    raw=struct.pack("i",2)+b"{}"
    with m.patch.object(oip.sys,"stdin") as st, m.patch.object(oip,"send_message") as sm:
      st.buffer.read.side_effect=[raw[:4],raw[4:]]; oip.main(); sm.assert_called_once(); self.assertFalse(sm.call_args[0][0]["success"])
