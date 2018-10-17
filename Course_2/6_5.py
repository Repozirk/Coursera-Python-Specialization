text = "X-DSPAM-Confidence:    0.8475";
num_st=text.find(":")
num_wsp=text[num_st+1:]
num_raw=num_wsp.strip()
num=float(num_raw)
print num
