def get_weather_icon(code):
    match code:
        case 0:
            return "sunny"
        case 1 | 2 | 3:
            return "cloudy"
        case 51 | 53 | 55 | 61 | 63 | 65 | 80 | 81 | 82:
            return "rainy"
        case _:
            return "sunny"  # default fallback


weather_icons = {
    "sunny": """\
    |
  \\ | /
   \\*/
--**O**--
   /*\\
  / | \\
    |""",
    "cloudy": """\
  .--.
 (    )
(______)""",
    "rainy": """\
    __   _
  _(  )_( )_
 (_   _    _)
/ /(_) (__)
/ / / / / /
/ / / / / /""",
}
