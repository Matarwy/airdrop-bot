class User:
    username = ""
    twitterUsername = ""
    discordUsername = ""
    walletAddress = ""
    referrals = []
    referred_by = ""
    process = ""


    def __init__(self, id, username, referred_by):
        self.userId = id
        self.username = username
        self.referred_by = referred_by


UserJsonModel = {
    "userId": "",
    "username": "",
    "twitterUsername": "",
    "discordUsername": "",
    "walletAddress": "",
    "referrals": [],
    "referred_by": "",
    "process": ""
}