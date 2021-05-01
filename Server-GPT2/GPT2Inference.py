import numpy as np
import torch
from transformers import (set_seed, TrainingArguments, Trainer, GPT2Config, GPT2Tokenizer,
                          AdamW, get_linear_schedule_with_warmup, GPT2ForSequenceClassification)


class GPT2:

    def __init__(self):

        # Look for gpu to use. Will use `cpu` by default if no gpu found.
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        # device = torch.device('cpu')
        print("Device: ", self.device)
        model_path = "Models\GPT2_Model\model"
        self.tokenizer = GPT2Tokenizer.from_pretrained(
            pretrained_model_name_or_path=model_path)
        self.gpt_model = GPT2ForSequenceClassification.from_pretrained(
            pretrained_model_name_or_path=model_path)
        self.gpt_model.eval()

    def predict(self, text):

        self.gpt_model.to(self.device)
        text = text[:1024]
        inputs = self.tokenizer(text, return_tensors="pt").to(self.device)
        # print(inputs)
        # inputs = inputs[:1024]
        outputs = self.gpt_model(**inputs)
        logits = outputs[0]
        predict_label = logits.argmax(axis=-1).flatten().tolist()
        return predict_label[0]

# The following code runs only while testing.
if __name__ == "__main__":

    sample = """Is it possible that our ancient ancestors knew the secrets of levitation? Technology that has since been lost in time and space?

Is it possible that great ancient civilizations like the ancient Egyptians, Olmec, Pre-Inca and Inca deciphered the secrets of levitation and other technologies that have been labeled by today’s society as impossible, mythological?

And if they did, is it possible that they used these ‘forgotten technologies’ to erect some of the most incredible ancient constructions on our planet?

There are dozens of amazing megalithic sites on our planet that defy our modern-day capabilities: Tiahuanaco, The Pyramids of the Giza plateau, Puma Punku, and Stonehenge among others. All of these sites were built using incredible blocks of stone that weight up to hundreds of tons, blocks of stone that our modern-day technologies have a hard time dealing with. So why did the ancient use such megalithic blocks of stone when they could have used smaller blocks and achieve a similar if not identical result?

Is it possible that ancient man possessed technologies that are lost today? Is it possible they had knowledge that surpasses our very own understanding? According to some researchers, it is possible that ancient man mastered the ‘art of levitation’ which allowed them to defy known physics and move and manipulate massive objects with extreme ease.

Tiahuanaco: defying modern-technology

13.000 feet above sea level stand the incredible ancient ruins of Tiahuanaco and its incredible ‘Sun Gate’. “La Puerta del Sol” or Sun Gate is an elaborately carved structure that is composed of stone blocks that weigh over ten tons. It is still a mystery how ancient managed to cut, transport and place these blocks of stone.

Temple of Jupiter Baalbek

The Temple of Jupiter located in Baalbek, Lebanon is another masterpiece of ancient engineering where huge blocks of stone were put together to form one of the greatest ancient sites on Earth. The foundation of the Temple of Jupiter contains three of the most massive stones ever quarried by mankind. The three foundation blocks together weigh 3.000 tons. If you ask yourself what type of vehicle would be used to transport them, the answer is NONE. Somehow, ancient man was able to quarry, transport and put them into place with such precision that not a single sheet of paper could fit in-between them.

At Baalbek, we have the ‘stone of the pregnant women’ which is one of the largest stones ever cut my mankind, with a weight of 1,200 tons.

Egyptian Pyramids: A mystery to mainstream science

The Egyptian pyramids are one of the ‘mission impossible’ constructions that have caused amazement among everyone who has had the opportunity to visit them. Even today, no one knows for a fact how ancient man was able to erect such marvelous structures. Mainstream science has proposed that it took a workforce of around 5000 men, working for twenty years to build them using ropes, ramps, and brute force.

Abul Hasan Ali Al-Masudi, known as the Herodotus of the Arabs wrote about how the ancient Egyptians built the pyramids in the distant past. Al-Mas’udi was an Arab historian and geographer and was one of the first to combine history and scientific geography in a large-scale work. Al-Masudi wrote about how ancient Egyptians transported the huge blocks of stone used to build the pyramids. According to him, a ‘magic papyrus’ was placed under each of the blocks of stone which allowed them to be transported. After placing the magical papyrus beneath the blocks, the stone was struck with a ‘metal rod’ that made the blocks of stone levitate and move along the path paved with stones and fenced on either side by metal poles. This allowed the stones to move for around 50-meters after which the process had to be repeated in order to get the blocks of stone to where they needed to be. Was Al-Masudi objective when he wrote about the pyramids? Or is it possible that just like many others, he was simply amazed by their magnificence, concluded that the ancient Egyptians must have used extraordinary means to construct the pyramids?

What if, levitation technology was present on Earth in the distant past and ancient civilizations like the Egyptians, Inca or Pre-Inca knew the secrets of levitation?

What if Levitation was possible in the past… but even today?
Is it possible that our ancient ancestors knew the secrets of levitation? Technology that has since been lost in time and space?

Is it possible that great ancient civilizations like the ancient Egyptians, Olmec, Pre-Inca and Inca deciphered the secrets of levitation and other technologies that have been labeled by today’s society as impossible, mythological?

And if they did, is it possible that they used these ‘forgotten technologies’ to erect some of the most incredible ancient constructions on our planet?

There are dozens of amazing megalithic sites on our planet that defy our modern-day capabilities: Tiahuanaco, The Pyramids of the Giza plateau, Puma Punku, and Stonehenge among others. All of these sites were built using incredible blocks of stone that weight up to hundreds of tons, blocks of stone that our modern-day technologies have a hard time dealing with. So why did the ancient use such megalithic blocks of stone when they could have used smaller blocks and achieve a similar if not identical result?

Is it possible that ancient man possessed technologies that are lost today? Is it possible they had knowledge that surpasses our very own understanding? According to some researchers, it is possible that ancient man mastered the ‘art of levitation’ which allowed them to defy known physics and move and manipulate massive objects with extreme ease.

Tiahuanaco: defying modern-technology

13.000 feet above sea level stand the incredible ancient ruins of Tiahuanaco and its incredible ‘Sun Gate’. “La Puerta del Sol” or Sun Gate is an elaborately carved structure that is composed of stone blocks that weigh over ten tons. It is still a mystery how ancient managed to cut, transport and place these blocks of stone.

Temple of Jupiter Baalbek

The Temple of Jupiter located in Baalbek, Lebanon is another masterpiece of ancient engineering where huge blocks of stone were put together to form one of the greatest ancient sites on Earth. The foundation of the Temple of Jupiter contains three of the most massive stones ever quarried by mankind. The three foundation blocks together weigh 3.000 tons. If you ask yourself what type of vehicle would be used to transport them, the answer is NONE. Somehow, ancient man was able to quarry, transport and put them into place with such precision that not a single sheet of paper could fit in-between them.

At Baalbek, we have the ‘stone of the pregnant women’ which is one of the largest stones ever cut my mankind, with a weight of 1,200 tons.

Egyptian Pyramids: A mystery to mainstream science

The Egyptian pyramids are one of the ‘mission impossible’ constructions that have caused amazement among everyone who has had the opportunity to visit them. Even today, no one knows for a fact how ancient man was able to erect such marvelous structures. Mainstream science has proposed that it took a workforce of around 5000 men, working for twenty years to build them using ropes, ramps, and brute force.

Abul Hasan Ali Al-Masudi, known as the Herodotus of the Arabs wrote about how the ancient Egyptians built the pyramids in the distant past. Al-Mas’udi was an Arab historian and geographer and was one of the first to combine history and scientific geography in a large-scale work. Al-Masudi wrote about how ancient Egyptians transported the huge blocks of stone used to build the pyramids. According to him, a ‘magic papyrus’ was placed under each of the blocks of stone which allowed them to be transported. After placing the magical papyrus beneath the blocks, the stone was struck with a ‘metal rod’ that made the blocks of stone levitate and move along the path paved with stones and fenced on either side by metal poles. This allowed the stones to move for around 50-meters after which the process had to be repeated in order to get the blocks of stone to where they needed to be. Was Al-Masudi objective when he wrote about the pyramids? Or is it possible that just like many others, he was simply amazed by their magnificence, concluded that the ancient Egyptians must have used extraordinary means to construct the pyramids?

What if, levitation technology was present on Earth in the distant past and ancient civilizations like the Egyptians, Inca or Pre-Inca knew the secrets of levitation?

What if Levitation was possible in the past… but even today?"""
    gpt = GPT2()
    print(gpt.predict(sample))
