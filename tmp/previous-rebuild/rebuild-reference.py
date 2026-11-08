from pathlib import Path
from html import escape
import re

def pos(x,y,w,h=0):
 return f'--x:{x:g};--y:{y:g};--w:{w:g};--h:{h:g}'
def art(cls,name,x,y,w,h,inner=None,flip=False,lazy=True):
 attrs=f'class="placed art {cls}{" flip" if flip else ""}" style="{pos(x,y,w,h)}" aria-hidden="true"'
 src=f'assets/original/{name}'
 if inner and inner[-1]:
  iw,ih,tx,ty,angle=inner
  content=f'<svg viewBox="0 0 {w} {h}" preserveAspectRatio="none"><image href="{src}" width="{iw}" height="{ih}" transform="translate({tx} {ty}) rotate({angle} {iw/2} {ih/2})"/></svg>'
 else:
  style=''
  if inner:
   iw,ih,tx,ty,_=inner
   style=f' style="width:{iw/w*100:.6f}%;height:{ih/h*100:.6f}%;left:{tx/w*100:.6f}%;top:{ty/h*100:.6f}%"'
  content=f'<img src="{src}" alt=""'+(' loading="lazy"' if lazy else ' fetchpriority="high"')+style+'>'
 return f'<div {attrs}>{content}</div>'
def textstyle(x,y,w,font,line):
 return pos(x,y,w)+f';--font:{font:g};--line:{line:g}'
def br(s): return escape(s).replace('|','<br class="desktop-break">')
about1='Im Neomii, I am a senior Marketing student at DePaul|University graduating with a Bachelors in Digital Marketing. I|have a strong interest in brand strategy, consumer behavior,|and research marketing.Ive been able to explore these|interests both in the classroom and outside.'
about2='I have built hands on experience throughout my career doing|content creation for Oud Cafe, and BobaNova. In these roles I|have supported brand visibility, developed social content, and|learned how to think strategically about how businesses show|up for their audiences.'
work1='A typical day in my internship|usually starts with looking at|what is happening in the cafe|that could be turned into|content. Since the space is|always active, there are a lot of|natural moments to capture.'
work2='From there, I film short clips,|think through captions, and|create posts or reels that match|Oud’s brand voice. Some of my|work is planned ahead, but a lot|of it also depends on noticing|small moments that could|connect with people online.'
exp1='My internship is a mix of in-|person and online work. The in-|person side is important|because I need to actually be in|the cafe to capture real content|and understand the customer|experience. The online side|comes in when I am editing|videos, writing captions,|checking engagement,|brainstorming content ideas,|and thinking about what types|of posts perform best.'
exp2='Oud is a smaller business|compared to a large corporate|company. Because the company|is more local, I get to see how|marketing decisions can directly|impact the business’s image and|customer connection.'
def paragraphs(*ps): return '\n'.join(f'<p>{br(p)}</p>' for p in ps)
# Keep whitespace at explicit desktop line breaks so the mobile copy reflows.
def paragraphs(*ps): return '\n'.join(f'<p>{br(p.replace("|", " |"))}</p>' for p in ps)
html=f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="Neomii Barron's marketing portfolio — brand strategy, consumer research, and social content.">
  <meta name="theme-color" content="#dbbec0">
  <title>Neomii Barron — Marketing Portfolio</title>
  <link rel="preload" href="assets/original/lovelace.woff" as="font" type="font/woff" crossorigin>
  <link rel="preload" href="assets/original/tenor-sans.woff" as="font" type="font/woff" crossorigin>
  <link rel="stylesheet" href="styles.css">
  <script src="script.js" defer></script>
</head>
<body>
<a class="skip-link" href="#about">Skip to about me</a>
<main>
  <section class="section hero" aria-labelledby="site-title">
    <div class="stage hero-stage">
      {art('hero-art','blue-tapestry.jpg',238.098672,43.370799,889.802657,681.258402,(684.025104,889.802657,102.888776,-104.272127,90),lazy=False)}
      <h1 id="site-title" class="placed text display hero-title" style="{textstyle(377.969713,246,606.2,154.423,138)}">Neomii<br>Barron</h1>
      <p class="placed text hero-subtitle" style="{textstyle(611.484202,524.16345,143.929404,19.9513,21)}">Marketing<br>Portfolio</p>
    </div>
  </section>

  <section class="section about blue" id="about" aria-labelledby="about-title">
    <div class="stage about-stage">
      <h2 id="about-title" class="placed text display about-title" style="{textstyle(76.8,132.577554,650.326132,135.72024,122.148216)}">About Me</h2>
      <div class="placed text about-copy" style="{textstyle(52.582803,272.798884,698.760526,22.849124,31.825508)}">
        {paragraphs(about1,about2)}
      </div>
      <figure class="placed portrait" style="{pos(783.744611,76.8,483.06087,614.4)}"><img src="assets/original/portrait.jpg" alt="Neomii Barron" width="1280" height="959"></figure>
      {art('about-lotus','pink-lotus.png',603.994823,4.390825,386.546629,270.692977,(270.692977,386.546629,57.926826,-57.926826,90))}
      {art('about-blossom','blossom-branch.png',661.863557,511.475481,389.016702,259.182378,(259.182378,389.016702,64.917162,-64.917162,90))}
    </div>
  </section>

  <section class="section resume" id="resume" aria-labelledby="resume-title">
    <div class="stage resume-stage">
      <h2 id="resume-title" class="placed text display resume-title" style="{textstyle(480.668216,13.628869,403.159494,60.16296,54.146664)}">My Resume</h2>
      {art('resume-lace','lace-frame.png',407.283794,57.162495,551.432411,653.67501,(551.432411,664.376399,0,-5.350695,0))}
      <a class="placed resume-link" style="{pos(482.401252,128.907173,419.566998,510.185653)}" href="NB%20Resume26.pdf" target="_blank" rel="noopener" aria-label="Open Neomii Barron’s resume PDF">
        <img src="assets/original/resume.png" alt="Preview of Neomii Barron’s resume" loading="lazy">
        <span class="hover-label">Open my resume ↗</span>
      </a>
      {art('cupid-left','cupid.png',41.203078,218.379219,287.102061,331.241562)}
      {art('cupid-right','cupid.png',1029.161032,201.823359,287.192531,331.34594,flip=True)}
    </div>
  </section>

  <section class="section work blue" id="work" aria-labelledby="work-title">
    <div class="stage work-stage">
      {art('work-art','tulips-paper.png',39.668423,-90.494173,500.272753,858.494173,(500.272753,889.373783,0,-15.439805,0))}
      <h2 id="work-title" class="placed text work-heading" style="{textstyle(607.736587,49.094238,150.526826,26.6664,28)}">Some of<br>my work</h2>
      <div class="placed text work-note" style="{textstyle(201.605491,293.832642,289.630547,18.061779,24.383646)}">
        {paragraphs(work1,work2)}
      </div>
      <div class="work-media">
        <video class="placed reel work-video" style="{pos(904.412839,76.8,334.745593,614.4)}" src="assets/oud-story.mp4" controls muted loop playsinline preload="metadata" aria-label="Oud Cafe social media video"></video>
        {art('rose-frame','rose-frame.png',813.518783,17.013354,516.533705,733.973293)}
      </div>
    </div>
  </section>

  <section class="section content" id="content" aria-label="More of my internship work">
    <div class="stage content-stage">
      <video class="placed reel content-video video-one" style="{pos(76.8,136.254137,273.749382,486.665567)}" src="assets/banana-matcha.mp4" controls muted loop playsinline preload="metadata" aria-label="Banana matcha social media video"></video>
      <video class="placed reel content-video video-two" style="{pos(558.828432,136.254137,271.551022,476.405301)}" src="assets/matcha-moments.mp4" controls muted loop playsinline preload="metadata" aria-label="Matcha preparation social media video"></video>
      {art('flower-divider','flower-border.png',404.410887,18.025494,100.417545,731.949013,(517.853927,731.949013,-1.632786,0,0))}
      {art('lilies-art','lilies-paper.png',876.09565,-75.064243,560.603222,846.193542,flip=True)}
      <div class="placed text experience-note" style="{textstyle(935.139336,218.596528,267.954844,17.134824,23.72532)}">
        {paragraphs(exp1,exp2)}
      </div>
    </div>
  </section>

  <section class="section paper blue" id="paper" aria-labelledby="paper-title">
    <div class="stage paper-stage">
      {art('paper-lotus','cream-lotus.png',-52,52.339667,286.944347,204.569848)}
      {art('paper-circle','pattern-circle.png',194.90848,-87.198461,1045.6686,1045.6686)}
      <h2 id="paper-title" class="placed text display paper-title" style="{textstyle(15.485788,37.519348,306.61475,59.38285,52.620625)}">Read my<br>paper on<br>my<br>internship!</h2>
      <div class="placed paper-document" style="{pos(533.003044,203.303067,369.479473,433.685169)}">
        <iframe src="https://docs.google.com/document/d/1eGzXeZUAS2v03SjrVd9bO0JtjfOlikiUp_sMi8sf8vA/preview?tab=t.0" title="Neomii’s internship paper — Final MKT393" loading="lazy"></iframe>
        <a href="https://docs.google.com/document/d/1eGzXeZUAS2v03SjrVd9bO0JtjfOlikiUp_sMi8sf8vA/preview?tab=t.0" target="_blank" rel="noopener">Read the full paper ↗</a>
      </div>
    </div>
  </section>

  <footer class="section contact" id="contact" aria-labelledby="contact-title">
    <div class="stage contact-stage">
      {art('contact-art','gold-tapestry.jpg',185.267903,44.996642,995.464194,678.006715,(698.069266,995.464194,148.697464,-158.72874,90))}
      <h2 id="contact-title" class="placed text contact-title" style="{textstyle(325.622334,272.607614,751.15625,98.3444,105)}">Contact me</h2>
      <a class="placed contact-link linkedin" style="{pos(558.521689,366.978296,81.7658,80.382567)}" href="https://www.linkedin.com/in/neomii-barron/" target="_blank" rel="noopener" aria-label="Neomii Barron on LinkedIn"><img src="assets/original/linkedin.svg" alt=""></a>
      <a class="placed contact-link email" style="{pos(755.952941,375.489148,91.292017,71.871715)}" href="mailto:nbarron280@gmail.com" aria-label="Email Neomii at nbarron280@gmail.com"><img src="assets/original/email.svg" alt=""></a>
      {art('contact-flower','hellebore.png',1093.649047,-21.082353,324.350953,324.350953)}
    </div>
  </footer>
</main>
</body>
</html>
'''
Path('index.html').write_text(html)
