from selenium import webdriver

def getCoins(holderID,thislist):
    driver = webdriver.Chrome("C:\\Users\\lenovo\\Desktop\\altCoin Data Analysis\\chromedriver")
    driver.get('https://bscscan.com/tokenholdings?a=' + holderID)
    driver.maximize_window()
    tokenSymbol=driver.find_elements_by_xpath('//tbody/tr/td[3]')


    with open('Coins.csv', 'w') as f:
            for token in tokenSymbol:
                thislist.append(token.text)
    driver.close()


i=0
def count():
    d = {x: thislist.count(x) for x in thislist}
    print({k: v for k, v in sorted(d.items(), key=lambda item: item[1])})


thislist=[]
#Green Moon
# getCoins('0x49393bc044289449cde2dfd31f5428eb4b911e53',thislist)
# getCoins('0x8692d45dbcd1cc3f4b7b183aa25f2a46985e3fc3',thislist)
# getCoins('0x9ec8e8f64ec6bb47d944b4b830130b5fcf2da182',thislist)
# getCoins('0x9c8a8e88ee393baa2bb18f70ccc00572af9a3dcc',thislist)
# getCoins('0x10e499b2e8a2f8487053708b0d99b5e9087da2b1',thislist)
# getCoins('0x7daa3d37672204c81249d3a4856c24e298ebf5a5',thislist)
# getCoins('0xa77a5594597f0f8198e5cc9dc82d628050cbe744',thislist)
# getCoins('0xf95cec072810cf79fe6d6c29f6f25b60f85112e1',thislist)
# getCoins('0xd5b93da93a61a739fb0f16359cfe8a460416f5ba',thislist)
# getCoins('0x650d5095cd33d90d3229c74170067ee7ddbc35d4',thislist)
# getCoins('0x315ba4e004390f784edc2a3d4a7b57496295b52d',thislist)
# getCoins('0x71ddecb092003b91697b3790aa45ecabfb1de260',thislist)
# getCoins('0x5191336f6373ef05d1648991e5bda94560e3225e',thislist)
# getCoins('0xc1142563315d50ab64838fe79b140da793347e28',thislist)
# getCoins('0xe3776e087a675d38877232985984d6fefc8cb193',thislist)
# getCoins('0xf2b6a11f404cae4c24adfa0e80a185e938954055',thislist)
# getCoins('0xa94758cf80d87de3f9ad7f67fbac2752ed477e1d',thislist)
# getCoins('0xf33802b83607aec5628eee76841dda93efba5581',thislist)
# getCoins('0x15929fa777644f841293772d992a767a752b9bc6',thislist)
# getCoins('0xa2f8a25b530350b9aae38be13b44cf596bdd937a',thislist)
# getCoins('0x7346ea29ad389f4e738521238fa451717c6bfd7c',thislist)
# getCoins('0xeef3431fb90f51251c87f9eb21af0df031ff3596',thislist)
# getCoins('0x8935a65d89cb8ca4e83203f2ec961c4418dfcfd5',thislist)
# getCoins('0x5239fc7bb50ca62c38b0ff89cea08eabbede1cc3',thislist)
# getCoins('0x53bd50b458d0c47dfa40b1f07a6a0e798cee93a6',thislist)
# getCoins('0x69a7223ca2e377f94a0981d9bc771e11ea15b477',thislist)
# getCoins('0xee73efab09cc7288b312c80c776dd0b1fec24d67',thislist)
# getCoins('0xd48fe6afcca78d2054b2f0194a072b20908d6df7',thislist)
# getCoins('0x06ce70106a21aa61816154cb0bcc7c9ae2d30750',thislist)
# getCoins('0x2829698c9b043104d9af77830c4510e5a8e3a65a',thislist)
# getCoins('0xab93b85fd25030e4800a9d190e2564809ede3518',thislist)
#

getCoins('0xc2f8ecdcb25c707b3becf4d3f00c24799f954f7a',thislist)
getCoins(' 0x1ae5e985ac41007d7430e763ef1694fd0b81f765',thislist)
getCoins('0xdf39e635d827a4ffaea5202cb41863b3dd35d775',thislist)
getCoins('0xc62c66643e231099553630146dd088c83f016aac',thislist)
getCoins('0x456811d8ce2428a8dafed6ba98a28f33ce4eee46',thislist)
getCoins('0x02eac76c53360371425dcdb0f57a7aa66d018cf8',thislist)
getCoins('0x1b19da858ac017b1af802331a5a0546a5ad0b1f7',thislist)
getCoins('0x40a47a0beabb373ffe090c9233eb4126dbaba882',thislist)
count()

