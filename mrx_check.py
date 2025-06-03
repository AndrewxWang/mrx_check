import sys
import requests
import html2text

def get_mrx(input):
  url = "https://mapleranks.com/u/" + input
  headers = {
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
  }

  response = requests.get(url, headers=headers)

  if response.status_code == 200:
      html_content = response.text

      text_maker = html2text.HTML2Text()
      text_maker.ignore_links = True
      text_maker.bypass_tables = False
      text = text_maker.handle(html_content)

      level_index = text.index("Lv. ")
      level_perc = text[level_index:level_index+18]
      level = level_perc[4:7]

      perc = level_perc[level_perc.index("(")+1:level_perc.index("%")]

      return level, perc
  else:
      print(f"Failed to retrieve page. Status code: {response.status_code}")
      return None, None

lvl_data = {
    200: 2207026470,  225: 49099398539,   250: 442457484960,   275: 11377111255510,
    201: 2471869646,  226: 52536356436,   251: 455731209508,   276: 12514822381061,
    202: 2768494003,  227: 56213901386,   252: 469403145793,   277: 13766304619167,
    203: 3100713283,  228: 60148874483,   253: 483485240166,   278: 15142935081084,
    204: 3472798876,  229: 64359295696,   254: 497989797370,   279: 16657228589191,
    205: 3889534741,  230: 83667084404,   255: 512929491291,   280: 33647601750165,
    206: 4356278909,  231: 86177096936,   256: 528317376029,   281: 37012361925183,
    207: 4879032378,  232: 88762409844,   257: 544166897309,   282: 40713598117701,
    208: 5464516263,  233: 91425282139,   258: 560491904228,   283: 44784957929471,
    209: 6120258214,  234: 94168040603,   259: 577306661354,   284: 49263453722418,
    210: 7956335678,  235: 122418452783,  260: 1731919984062,  285: 99512176519285,
    211: 8831532602,  236: 126091006366,  261: 1749239183902,  286: 109463394171214,
    212: 9803001188,  237: 129873736556,  262: 1766731575741,  287: 120409733588335,
    213: 10881331318, 238: 133769948652,  263: 1784398891498,  288: 132450706947169,
    214: 12078277762, 239: 137783047111,  264: 1802242880412,  289: 145695777641885,
    215: 15701761090, 240: 179117961244,  265: 2342915744535,  290: 294305470836608,
    216: 17114919588, 241: 184491500081,  266: 2366344901980,  291: 323736017920269,
    217: 18655262350, 242: 190026245083,  267: 2390008350999,  292: 356109619712296,
    218: 20334235961, 243: 195727032435,  268: 2413908434508,  293: 391720581683526,
    219: 22164317197, 244: 201598843408,  269: 2438047518853,  294: 430892639851879,
    220: 28813612356, 245: 262078496430,  270: 5412465491851,  295: 870403132500795,
    221: 30830565220, 246: 269940851322,  271: 5466590146770,  296: 957443445750874,
    222: 32988704785, 247: 278039076861,  272: 5521256048237,  297: 1053187790325960,
    223: 35297914119, 248: 286380249166,  273: 5576468608720,  298: 1158506569358560,
    224: 37768768107, 249: 294971656640,  274: 5632233294807,  299: 1737759854037840
}

commands = {
    "!gain",
    "!goal",
    "!help",
    "!quit"
}

def main():
    level, perc_str = get_mrx((input("enter ign: ")))

    perc = float(perc_str)

    print("current level: " + level)
    print("current percent(%): " + perc_str + "%")

    total_exp = lvl_data[int(level)]

    one_tril = 1000000000000
    one_percent = total_exp / one_tril

    while True:
        print("")
        inp = input("enter command (!help for commands): ")

        if inp == "!gain":
            while True:
                try:
                    curr_exp = float(input("enter current exp (enter -1 to quit): "))

                    if curr_exp == -1:
                        break

                    exp_gained = ((curr_exp-perc)*one_percent) / 100
                    rounded_exp_gained = round(exp_gained, 3)

                    print("exp gained today (in T): " + str(rounded_exp_gained) + "T")
                except ValueError:
                    pass
       
        elif inp == "!goal":
            goal = int(input("enter exp goal (T): ")) * one_tril
            
            goal_perc_inc = 100 - ((total_exp - goal)/total_exp)*100
            goal_perc = round(perc + goal_perc_inc, 3)

            print("current percent: " + str(perc) + "%")
            print(str(goal/one_tril) + "T = " + str(round(goal_perc_inc, 3)) + "% net percent")
            print("you need to reach " + str(goal_perc) + "% to do " + str(goal/one_tril) + "T exp!")

        elif inp == "!help":
            print("command list: ")

            for comm in commands:
                print(comm)
       
        elif inp == "!quit":
            break
       
        else:
            pass
            # continue on until user types quit

main()