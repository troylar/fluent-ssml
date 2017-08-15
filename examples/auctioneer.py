from fluentssml import FluentSSML

fs = FluentSSML()
s = fs.rate_inc(60).txt_x("I'm at 500 and I want 550") \
      .vol_x_loud().txt("550") \
      .rate_inc(60).txt("bid on 550 Im at 500 would you go 550 550 for the " +
                        "gentleman in the corner") \
      .rate_inc(90).txt("A big black bug bit a big black bear a big black bug" +
                        "bit a big black bear").txt("Do we get 600?") \
      .rate_inc(90).txt("A big black bug bit a big black bear") \
      .rate_inc(60).txt("We got 600 for the whole herd") \
      .rate_def().vol_x_loud().txt("Sold") \
      .rate_inc(60).txt("for 600") \
      .ssml
print s
