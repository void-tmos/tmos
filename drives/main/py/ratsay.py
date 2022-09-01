try:
    args[0][0]
    message = " ".join(args)
except:
    message = random.choice(open(file("/etc/tips"), "r").read().splitlines())

length = len(message)

print(r"""
  %s
 < %s >
  %s
    \    (\,/)
     \   oo   '''//,        _
       ,/_;~,        \,    / '
       "'   \    (    \    !
             ',|  \    |__.'
             '~  '~----''
""" % ("_"*(length+2), message, "_"*(length+2)))