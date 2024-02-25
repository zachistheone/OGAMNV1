import fortnitepy
import json
import os

# let this like that for now, ill finish the code later.

async def wait_for_user_input(ctx, client) -> str:
    def check(m):
        return m.channel.id == ctx.channel.id and m.author.id == ctx.author.id
    hmmm = await client.wait_for("message", check=check, timeout=60)
    return hmmm

class FortniteBotClient(fortnitepy.Client):
    # if u think its a way to hack people, here is the obvious response: NO.
    # if it DID hack you, open an issue at https://github.com/zachistheone/OGAMNV1
    def __init__(self, email, password, ctx, client):
        self.ctx = ctx
        self.client = client
        device_auth_details = self.get_device_auth_details().get(email, {})
        super().__init__(
            auth=fortnitepy.AdvancedAuth(
                email=email,
                password=password,
                prompt_authorization_code=True,
                prompt_code_if_invalid=True,
                delete_existing_device_auths=True,
                **device_auth_details
            )
        )

    def get_device_auth_details(self, filename):
        # idk why u need to put a filename
        if os.path.isfile(filename):
            with open(filename, "r") as fp:
                return json.load(fp)
        return {}
    
    def store_device_auth_details(self, email, details, filename):
        existing = self.get_device_auth_details()
        existing[email] = details

        with open(filename, "w") as fp:
            json.dump(existing, fp)

    async def event_device_auth_generate(self, details, email, filename):
        self.store_device_auth_details(email, details, filename)
    
    async def event_ready(self):
        await self.ctx.send(f'----------------\nClient ready as\n{self.user.display_name}\n{self.user.id}\n----------------')
    
    async def event_friend_request(self, request):
        await self.ctx.send("A friend request has been sent.\nDo you accept? (Y/N)")
        message = await wait_for_user_input(self.ctx, self.client)
        if message.lower() == "y":
            request.accept()
        else:
            request.decline()
    
    async def event_friend_message(self, message):
        await self.ctx.send("Received message from {0.author.display_name} | Content: \"{0.content}\"\nWhat do you want to respond?".format(message))
        reply = await wait_for_user_input(self.ctx, self.client)
        await message.reply(reply)