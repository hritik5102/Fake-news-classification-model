# all the imports
import os

from fakenews_detector.fake_fact_ai.finalModel import model
from fakenews_detector.fake_fact_ai.settings import APP_STATIC

mod = model(fakeFile=os.path.join(APP_STATIC, 'fake2.txt'), realFile=os.path.join(APP_STATIC, 'real2.txt'))
