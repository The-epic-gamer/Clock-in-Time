from typing import Optional
import discord
import asyncio
import time
import mysqlcontrol
import discordkeysmain
from discord.ext import commands, tasks
token = discordkeysmain.token
def bot1():
    intents = discord.Intents.all() 
    client = commands.Bot(command_prefix='.',intents=intents)
    def checkindex(interaction):
        if indexindices:
            if interaction.user in indexindices:
                pass
            else:
                indexindices[interaction.user] = userindex()
        else:
            indexindices[interaction.user] = userindex()
            return indexindices[interaction]
    class node:
        def __init__(self, left, right):
            self.right = right
            self.left = left
            self.time = None
            self.title = None
            self.description = None
        def get_tot(self):
            min_sum = self.right[1]-self.left[1]
            hour_sum = self.right[0]-self.left[0]
            if min_sum<0:
                print(min_sum)
                min_sum = 60+(min_sum)
                hour_sum-=1
            self.time = [hour_sum,min_sum] 
    class userindex:
        def __init__(self):
            self.data = [[0,0]]
            self.userindices = []
        def time_fill(self):
            for x in self.userindices:
                x.get_tot()
        def sakujyu(self):
            word = self.data
            outputlist = self.userindices
            if len(outputlist) ==0:
                for x in range(len(word)):
                    j = x+1
                    if x==len(word) or j==len(word):
                        return
                    outputlist.append(node(word[x], word[j]))        
            else:
                for x in range(len(word)-1):
                    if len(word)>len(outputlist)+1:
                        try:
                            if not (outputlist[x].right == word[x+1] and x+1!=len(word)):
                                outputlist.insert(x,node(word[x],word[x+1]))
                                outputlist[x+1].left = word[x+1]
                                return
                        except IndexError:
                            outputlist.append(node(word[x],word[x+1]))
                    else:
                        if (outputlist[x].right != word[x+1]) or (x+1)==len(word)-1:
                            outputlist[x].left = word[x]
                            outputlist[x].right = word[x+1]
                            outputlist.pop(x+1)
                            return
                        elif (x+1)==len(word)-1:
                            outputlist.pop(-1)
                            return
                        elif len(outputlist)==1:
                            outputlist.clear()
                            return  
        def insertion_func(self, subarray :str):
            input_list = self.data
            tmp = []
            tmp.append(int(subarray[0:2]))
            tmp.append(int(subarray[3:5]))
            subarray = tmp
            print(subarray)
            first = subarray[0]
            last = subarray[1]
            if(len(input_list)==0):
                return input_list.append(subarray)
            for x in range(len(input_list)):    
                j = x
                j-=1
        
                if(input_list[x][0]>first and (first>=input_list[x-1][0] or x==0)) or (x==len(input_list)-1):
                    if first>input_list[x][0]: 
                        input_list.insert(x+1,subarray)
                        self.sakujyu()
                        return input_list
                    if first>input_list[x][0] and last<input_list[x][1]:
                        input_list.insert(x+1,subarray)
                        self.sakujyu()
                        return input_list
                    if first==input_list[x][0] and last>input_list[x][1]:
                        input_list.insert(x+1,subarray)
                        self.sakujyu()
                        return input_list
                    while j>0 and input_list[j][1]>last and input_list[j-1][0]==first and first==input_list[j][0]:
                        if j<0 or j==-1:
                            j+=1
                            break
                        j-=1
                    if (first>input_list[j][0]):
                        input_list.insert(j+1,subarray)
                        self.sakujyu()
                        return input_list
                    if (first==input_list[j][0] and last>input_list[j][1]):
                        input_list.insert(j+1,subarray)
                        self.sakujyu()
                        return input_list
                    input_list.insert(j, subarray)
                    self.sakujyu()
                    return input
        def poplist(self, user_input):
            tmp = []
            tmp.append(int(user_input[0:2]))
            tmp.append(int(user_input[3:5]))
            self.data.remove(tmp)
            self.sakujyu()
            return self.data
        def clock_in(self):
            self.embed = discord.Embed(color=discord.Color.dark_green(),title="Clock in Time")
            for x in self.data:
                self.embed.add_field(name=f"Time {x}\n",value=" ",inline=False)
                
                
                    
        def embedreel(self):
            self.embed = discord.Embed(color=discord.Color.dark_green(),title="What you did Today")
            for x in self.userindices:
                print(x.left, x.right, x.time, x.title)
                self.embed.add_field(name=f"\n{x.left} <-> {x.right}", value=f"{x.time} ->{x.title}",inline=False)
        def to_dict(self):
            return self.embed.to_dict()
        def insert_assignment(self, argu:str,argu2:str):
            self.userindices[int(argu)].title = argu2
    class persistentbut(discord.ui.View):
        def __init__(self):
            super().__init__(timeout=None)
        @discord.ui.button(label="Stopwatch",custom_id="button1",style=discord.ButtonStyle.success)
        async def persistent_button_callback(self, interaction:discord.Interaction,button: discord.Button):
            if indexindices:
                if interaction.user in indexindices:
                    pass
                else:
                    indexindices[interaction.user] = userindex()
            else:
                indexindices[interaction.user] = userindex()
            indexindices[interaction.user].insertion_func(time.strftime("%H:%M",time.localtime()))
            indexindices[interaction.user].clock_in()
            await interaction.response.send_message(embed=indexindices[interaction.user])
        @discord.ui.button(label="record",custom_id="button2",style=discord.ButtonStyle.danger)
        async def persistent_button_callback2(self, interaction:discord.Interaction,button: discord.Button):
            if not checkindex(interaction.user).userindices:
                await interaction.response.send_message(f"{interaction.user} pressed me! {indexindices.get(interaction.user).data}")
            else:
                checkindex(interaction.user).time_fill()
                checkindex(interaction.user).embedreel()
                await interaction.response.send_message(embed=checkindex(interaction.user))
    @client.event 
    async def on_ready():
        print("Hello world from bot 404")
        msg1.start()
        client.add_view(persistentbut())
        global indexindices
        indexindices = {}
    @tasks.loop(hours=24)
    async def msg1():
        client_help = client.get_channel(971696970706079784)
        await client_help.send(f"test {time_object}")
    @msg1.before_loop
    async def before_msg1():
        for _ in range(360*24):
            global time_object
            time_object = time.localtime()
            if time.strftime("%H:%M", time_object) == "00:00":
                print("its gamer time")
                return
            await asyncio.sleep(2)
            print(time.strftime("%H:%M:%S", time_object))
    @client.command()
    async def button(ctx):
        embed = discord.Embed(
            color=discord.Colour.gold(),
            title="StopWatch++",
            description="Please press the button to the left to register at time of completion and press the button to the right to print your daily log"
        )
        await ctx.send(view=persistentbut(),embed=embed)
        await ctx.message.delete()
    @client.command()
    async def insert(ctx, arg):
        author = ctx.author
        checkindex(author).insertion_func(arg)
        checkindex(ctx.author).time_fill()
        checkindex(ctx.author).embedreel()
        await ctx.send(embed=checkindex(ctx.author))
        await ctx.message.delete()
    @client.command()
    async def pop(ctx, arg):
        author = ctx.author
        checkindex(author).poplist(arg)
        checkindex(ctx.author).time_fill()
        checkindex(ctx.author).embedreel()
        await ctx.send(embed=checkindex(ctx.author))
        await ctx.message.delete()
    @client.command()
    async def insert_work(ctx, arg, arg2):
        checkindex(ctx.author).insert_assignment(arg, arg2)
        checkindex(ctx.author).time_fill()
        checkindex(ctx.author).embedreel()
        await ctx.send(embed=checkindex(ctx.author))
        await ctx.message.delete()
            
        
    client.run(token)
if __name__ == "__main__":
    bot1()