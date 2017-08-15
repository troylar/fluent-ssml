from fluentssml import FluentSSML

fs = FluentSSML()
s = fs.rate_inc(50).txt("Sale, sale, sale.") \
      .rate_def().vol_x_loud().txt("Today!").break_m() \
      .txt("Call").rate_dec(30).say_as_phone().txt("202-555-1212") \
      .ssml
print s
