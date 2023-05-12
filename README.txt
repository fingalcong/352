Yinfeng Cong netid: yc957

I implement this by reading data of HNS in client first, and send them into RS (I read DNSRS in RS) to check if these HNS are included in the
list of DNSRS, then I returned the data back to client, and sent the data with "NS" again to TS, and check if these data are included in the list
of DNSTS. Then, I sent back again to client. I also saved these data together, and output them as "resolved".

I personally think that there are not any issues in, that is also the reason why I asked my TA - Mr.Patel for many times.

I faced many problems, I did not know python much. So I did not know how to use in to check if the hostname was included in RS.
Also, I did not know how to save the data of client from RS, to help me know which data should I sent to TS.
I solved both of these problems by asking for help from TA and my friend, also by self-learning from the websites.

I learned a lot about the use of python, and I learned about how to build a DNS like this. I spent alomost a week on this project, and I think it is really worthy.

