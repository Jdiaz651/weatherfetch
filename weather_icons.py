def get_weather_icon(code):
    match code:
        case 0:
            return "Sunny"
        case 1 | 2 | 3:
            return "Cloudy"
        case 51 | 53 | 55 | 61 | 63 | 65 | 80 | 81 | 82:
            return "Rainy"
        case _:
            return "Sunny"  # default fallback


weather_icons = {
    "Sunny": """\
    |
  \\ | /
   \\*/
--**O**--
   /*\\
  / | \\
    |
""",
    "Cloudy": """\
  .--.
 (    )
(______)
""",
    "Rainy": """\
    __   _
  _(  )_( )_
 (_   _    _)
/ /(_) (__)
/ / / / / /
/ / / / / /
""",
}
