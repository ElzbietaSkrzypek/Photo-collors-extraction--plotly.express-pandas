import pandas
from PIL import Image
import extcolors
from colormap import rgb2hex
import plotly.express as px


# --------- Get colors----------------#

img = Image.open("Your photo path.png")
# set tolerance and limit to define how many colors you want to extract, I chose 12 so 12 colors will be extracted.
colors, pixel_count = extcolors.extract_from_image(img, tolerance=12, limit=12)

# ------------rgb2hex -----------------#

color_hex_list = []
coloro_list = []
 #coloro - stands for color occurency

for color in colors:
    colorrgb = color[0]
    coloro = color[1]
    color_hex = rgb2hex(colorrgb[0], colorrgb[1], colorrgb[2])
    color_hex_list.append(color_hex)
    coloro_list.append(coloro)

color_dict = {"color_hex": color_hex_list, "coloro": coloro_list}

# -------------DataFrame------------ #

colors_df = pandas.DataFrame(color_dict)

# ------------Donut char--------------#

fig = px.pie(labels=colors_df.color_hex,
             values=colors_df.coloro,
             names=colors_df.color_hex,
             hole=0.6,
             title="Donut chart showing the percentage of the colors from the image.",
             color_discrete_sequence=colors_df.color_hex)
fig.update_traces(textposition='inside', textinfo='percent+label')
fig.update_layout(title={'x': 0.5,'xanchor': 'center'},
                  legend={'orientation': "h", 'yanchor': "top", 'y': 0, 'xanchor': "right", 'x': 1})

fig.show()

# Any figure can be saved as an HTML file using the write_html method.
# These HTML files can be opened in any web browser to access the fully interactive figure.
# fig.write_html("path/to/file.html")

