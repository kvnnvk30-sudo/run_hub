from pptx import Presentation
from pptx.util import Pt

# Create a new PowerPoint presentation
prs = Presentation()

# Title Slide
title_slide_layout = prs.slide_layouts[0]
slide = prs.slides.add_slide(title_slide_layout)
title = slide.shapes.title
title.text = "My Python-Pptx Presentation"
subtitle = slide.placeholders[1]
subtitle.text = "A simple example"

# Content Slides
content_slide_layout = prs.slide_layouts[5]

# Slide 1
slide = prs.slides.add_slide(content_slide_layout)
title = slide.shapes.title
title.text = "Slide 1"
content = slide.placeholders[0]  # Use 0 for content placeholder
content.text = "This is the content of slide 1."

# Slide 2
slide = prs.slides.add_slide(content_slide_layout)
title = slide.shapes.title
title.text = "Slide 2"
content = slide.placeholders[0]  # Use 0 for content placeholder
content.text = "This is the content of slide 2."

# Bullet Points Slide
bullet_slide_layout = prs.slide_layouts[1]
slide = prs.slides.add_slide(bullet_slide_layout)
shapes = slide.shapes
title_shape = shapes.title
title_shape.text = "Bullet Points Slide"
text_box = shapes.add_textbox(left=100, top=100, width=500, height=300)
tf = text_box.text_frame
tf.text = "Bullet Points"
p = tf.add_paragraph()
p.text = "Point 1"
p.space_after = Pt(14)
p = tf.add_paragraph()
p.text = "Point 2"
p.space_after = Pt(14)
p = tf.add_paragraph()
p.text = "Point 3"

# Save the presentation to a file
prs.save("my_complex_presentation.pptx")