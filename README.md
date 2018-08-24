# qbot

Remember back in the day when you could go online and buy things without any concerns? Well those times are long over and we now live in the era of bots. These bots are terrible and horrible creations that prevent everyday people like myself from buying things online. So if you can't beat 'em, join 'em. That's why I've made my own bot here for me and everyone to use. This bot has been generally structured using thechinatownmarket.com and will be optimized for supremenewyork.com once their website is available to use again on August 20th 2018.


### Setup

Sorry to non-OSX users but I built this program exclusively on my macbook so you might have to go a little bit further out of your way to get this set up properly. If you have a mac pretty much all you have to do is copy and paste the following commands, I added descriptions if you want an in depth.

```
pip install selenium
```

This command will install selenium, a tool used for web automation. This tool is what lets us control the web browser; e.g. going to web pages, clicking links, waiting for things to load on the page, etc.

Next you're going to want to [click this](https://chromedriver.storage.googleapis.com/index.html?path=2.41/) and choose your operating system to install ChromeDriver, a web driver for Google Chrome. A web driver essentially allows us to carry out automated actions in a browser. Selenium needs a web driver in order to work; you could also use Firefox, Safari, or whatever browser but I like Chrome. 


Lastly you'll want to unzip the file we just downloaded and run the following commands in the terminal. If you don't know how to open the terminal just press COMMAND + SPACE and search for the word "terminal". Once you're there copy and paste these commands in and press enter.

```
cd Downloads
mv chromedriver /usr/local/bin
```

The "cd Downloads" command is going to the directory on your computer that contains all of your downloads. The command after that is just moving chromedriver to a different directory on your computer called "user/local/bin". This a space in your computer commonly and optimally used for putting these types of resources. 

And that's it, you're now fully set up and ready to use my bot! (sorry for non osx people who couldn't get things set up yet. you were smart enough not to get a mac so i'm sure you're smart enough to figure it out, i believe in you)


### Usage

When using this program, there is a very specific set of steps necessary to ensure that it runs as desired. Make sure to precisely follow each of these steps and everything will hopefully run smoothly.

#### Know What You Want

The first and most important step is to know what exactly it is you want to get. That means know what is dropping for the week, what size you want, and what colourway you want. The best place to start this would be to either check on [/r/supreme](https://www.reddit.com/r/supremeclothing/) or [this guy on twitter](https://twitter.com/DropsByJay). These resources should have the information regarding the week's drop two or three days before. Once you pick all of the pieces you like, you need to know their exact name and what category they fall under. You can use the [supreme preview page](https://www.supremenewyork.com/previews/fallwinter2018/all) to get this information.

#### Inputing Information

Once you have all the information regarding the pieces you want, you can now run the setup.py file to get everything ready. Type the command below into your terminal to start the program, this program will ask you for all the relevant information in order for the bot to work. Also don't worry I won't have access to any information you write into the setup.py.

```
python setup.py
```

I will now include some important things to remeber when entering data in each field. As a general reminder, make sure to type "yes" just like that each time you want to confirm a section. 

##### Google
* When entering your email, make sure to include @whatever.com at the end, even if it is @gmail.com.

##### Clothing
* When inputting the name of the clothing item, make sure to have the first letter of each word capital and the rest lower case. Exactly how it is listed on the preview page. e.g. Dragon Work Jacket, Supreme Steiff Bear, Split Logo S/S Top, etc.
* When inputting the size of the clohting item, ensure that the first letter is captial. The only special case is extra large. All of the sizes go as follows; Small, Medium, Large, XLarge.
* If a clothing item does not have a size (bags, accessories, bikes) write "OS" exactly.
* When inputting the category of the clothing item, write it all lowercase. Just look at the extension on the supreme preview page. The only special cases are t-shirts (which will be "t-shirts") and tops/sweater (which will be tops_sweaters).
* The colour index is a little tricky. If your clothing item doesn't have a colour option or only has one colour just put 1. If the item has multiple colours, the best way to ensure you get the colour you like is to check the EU supreme site when the clothes drop for them at 11:00 AM GMT. I'll let you calculate when that is for you on your own but in order to access the EU site you'll have to use an EU proxy. I've found [this one](http://www.uk-proxy.co.uk/) to work pretty well. All you go is go to supreme once the items have dropped. Go to the item you want and see when index the colour you want is. If it's the second colour, it's 2. If it's the third colour, it's 3. You can see where I'm going with this.

##### Shipping
* Capitalization of first and last name don't matter too much, just make sure it matches the name on whatever card you plan to by with.
* Enter your phone number raw, no symbols. If your number is +1 (800)-123-4444 it would just be 8001234444.
* So the city and state actually don't matter at all because I didn't know they get all that information from the zip code. I was just too lazy to code it out I'll fix it later. I would still just enter that information correctly for your own sake. Just ensure that your zip is correct.

##### Billing
* Enter your card number raw. So if it's 1111 2222 3333 4444 then type 1111222233334444.
* Enter your expiration month with leading zeros, so put 03 not 3.
* Enter your expiration year as the full year. If it's 23 on your card then type 2023.

#### Running the Program

There is a very specific way in which the program runs. You should familiarize yourself before actually running the program. First off we want to start the program. To do this run the following command:

```
python app.py
```

This command will start running the program. First the program is going to automatically sign you in to google. It does this so that when you perform the captcha tests it will store the token with your account. 

Next you will manually go to google in the search barand search for "recapthca demo". Click the first link and you should be on a page with a captcha test. Don't start this test until about 2 minutes before the drop, the tokens only last about a minute and a half. It may take a little longer than your are used to because we are using an automated testing environment so it may pick up on that. Once you have done this the computer will wait until 3 seconds before the supreme drop. Once it is within three seconds, it will go to the site and refresh until the drop occurs.

The program will then one by one add everything to your cart, take you to checkout, enter your billing and shipping info, and check the accept of terms and conditions. The very last step is to manually hit the checkout button. I've done this to ensure that you yourself can review the order/information before actually sending your money to supreme.

These are are the necessary steps in order to use my bot to get some supreme. I hope that everything went smoothly getting to this point and I wish you good luck cooking!

### Authors

* **Qasim Shareh** - pretty much all development


### Aknowledgements

* Shoutout to GE Digital for introducing me to the simple wonders of Selenium
* Shoutout to Supreme for making me victim to hypebeast culture
* Should out to my cat Petra, my sister j'smol, my mom the mayor, and my dad the doc
