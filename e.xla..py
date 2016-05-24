def Enigma( A, B, C, D, E) :
     CM=0
     CMn=0
     CI =0
     J=( A+B+C+D+E) / 5
     if A>J:
         CM=CM+1
     else:
         if A<J:
             CMn=CMn+1
         else:
             CI =CI +1
     if B>J:
         CM=CM+1
     elif B<J:
         CMn=CMn+1
     else:
         CI =CI +1
     if C>J:
         CM=CM+1
     else:
         if C<J:
             CMn=CMn+1
         else:
             CI =CI +1
     if D>J:
         CM=CM+1
     elif D<J:
         CMn=CMn+1
     else:
         CI =CI +1
     if E>J:
         CM=CM+1
     elif E<J:
         CMn=CMn+1
     else:
         CI =CI +1
     print (CM, CMn, CI)

Enigma( 10, 4, 6, 15, 3)
