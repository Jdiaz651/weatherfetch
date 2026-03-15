from multiprocessing import Condition

weather_icons = {
    "sunny": """
    |
  \\ | /
   \\*/
--**O**--
   /*\\
  / | \\
    |
""",
    "cloudy": """
  .--.
 (    )
(______)
""",
}

condition = "sunny"
print(weather_icons[condition])
