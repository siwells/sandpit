/*
* On OS X use the following to play:
*   $ ./a.out | sox -t raw -r 8k -c 1 -e unsigned -b 8 - -d
*
*   t*((t>>3|t>>9)&82&t>>9)
*   t*((t>>12|t>>8)&63&t>>4)
*   t*((t>>9|t>>13)&25&t>>6)
*   t*((t>>9|t>>8)&63&t>>4)
*   t*((t>>11|t>>8)&123&t>>3)
*   t*((t>>5|t>>8))>>(t>>16)
*   t*( t>>8*(t>>15|t>>8) & (20|(t>>19)*5>>t|t>>3))
*   (-t&4095)*(255&t*(t&t>>13))>>12+(127&t*(234&t>>8&t>>3)>>(3&t>>14))
*   ((((5&((3 *(23*(4^t)))+t))*(9*((15>>((9&((t&12)^15))>>5))*2)))*((((t*(t*8))>>10)&t)>>42))^15) 
*   t * ( ((t>>9)&10) | ((t>>11)&24) ^((t>>10)&15&(t>>15)) ) 
*   t&(t>>9)&31
*   (t&t>>13|t>>6)
*   (t|t>>9)
*   (t*5&t>>7)|(t*3&t>>10)
*   t>>6^t&0x25|t+(t^t>>11)-t* ((t%24?2:6)&t>>11)^t<<1&(t&0x256?t>>4:t>>10)
*   (t*t*t)>>t 
*   ((t+13217)/1211)&(t>>2|t>>4|t>>6)
*   ((t+13217)/1211)&(t>>2|t>>4|t>>6)|(t>>2)|(t%256)
*   t*((t+13217)/1211)&(t>>2|t>>4|t>>6)/512
*   ((t*(t>>8|t>>9)&(t/256+45)&t>>8))^(t&t>>13|t>>6)
*   (t/384)&(t<<3|t>>3)+(t/896)&(t<<5|t>>5)+(t/1664)&(t<<7|t>>7)
*   (t*t/256)&( t>>((t/1024)%16) )
*   ((t*t)>>((((8*t)&(t>>t))>>((11>>t)&(8|8)))+(((t+8)*((((t|11)*(t+11))+((t&8)>>(t+11)))*(((11>>8)|(t|8))>>((t>>8)|(11&8)))))+((t>>11)-(8|11)))))
*   20 * t*t* (t >>11)/7
*   16 * t*t* (t >>11)/7
*   (t>>13|t%24)&(t>>7|t%19)
*   ((1-(((t+10)>>((t>>9)&15))&2))*2)*((((t)>>10)^((t+20)>>10))&1)*32+(((t&4095)-2047)*((t/((t>>10&3)+1))&((t>>10&7)+5))+(t>>(((t>>12)+16)&25)&1)*t%512*(t%256-128)/2)/1024+128 
*   ((1-(((t+10)>>((t>>9)&((t>>14))))&(t>>4&-2)))*2)*(((t>>10)^((t+((t>>6)&127))>>10))&1)*32+128
*   t>>6^t&0x25|t+(t^t>>11) -t*((t%24?2:6)&t>>11)^t<<1 &(t&0x256?t>>4:t>>10)
*   (~t/100|(t*3))^(t*3&(t>>5))&t
*   t*(t>>9|t>>13)&16
*   ( t* (( t>>9| t>>13 ) & 15)) & 129
*   (t%31337>>3)|(t|t>>7)
*   (t&t>>7)*((1+t/4096)%2)
*   (int)(((t>>4)|(t%10))+3.3) | (((t%101)|(t>>14))&((t>>7)|(t*t%17)))
*   t*((t>>11&t>>8)&123&t>>3)
*   (t<65536)?((2*t*(t>>11)&(t-1)|(t>>4)-1)%64):(((t%98304)>65536)?((17*t*(2*t>>8)&(t-1)|(t>>6)-1)%64|(t>>4)):((15*t*(2*t>>16)&(t-1)|(t>>8)-1)%64|(t>>4))) 
*   ((t*5/53) | t*5+(t<<1))
*   (t|t>>5)&(t|t>>13)-(t|t>>21)
*   (t*3|t*2>>7)+(t*2&t*3>>8)+(t*2&t>>8)
*   (t>>7|t|t>>6)*10+4*(t&t>>13|t>>6)
*   (t>>6|t|t>>(t>>16))*10+((t>>11)&7)
*   (t|(t>>9|t>>7))*t&(t>>11|t>>9)
*   t*5&(t>>7)|t*3&(t*4>>10)
*   (t>>7|t|t>>6)*10+4*(t&t>>13|t>>6)
*   ((t&4096)?((t*(t^t%255)|(t>>4))>>1):(t>>3)|((t&8192)?t<<2:t))
*   ((t*(t>>8|t>>9)&46&t>>8))^(t&t>>13|t>>6)
*   (t*5&t>>7)|(t*3&t>>10)
*   (int)(t/1e7*t*t+t)%127|t>>4|t>>5|t%127+(t>>16)|t
*
*   for(t=0;;t++)
*        putchar(
*            v=(v>>1)+(v>>4)+t*(((t>>16)|(t>>6))&(69&(t>>9)))
*        );
*
*/

main(t)
{
    for(t=0;;t++)
        putchar(
            (int)(t/1e7*t*t+t)%127|t>>4|t>>5|t%127+(t>>16)|t
        );
}
