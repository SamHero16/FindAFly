This project arose from a real problem. Me and my friends were going to go fly fishing, and I had a box of flies my dad had given me years ago. I looked down and didn’t recognize a single fly. I decided to make a Convolutional Neural Net that could classify the flies in my box. I could not find a fly classifier on the internet, so I was pleased that the idea was some novel. 

My first question was what flies I should include in my model. I can’t include every fly every created, but I wanted the user to be able to classify any fly in his box. So I went to the fly shop and asked around, and settled on 22 of the most popular flies I could find. 

I began to think of how to gather data. First, I went online and mass downloaded every picture of each fly available on Google Images. All of these were close-up, high-definition images of flies with nice backgrounds. I trained my model, but it did not generalize well to pictures from a phone camera, which was the whole point of my model.

I realized I needed to go into the fly shop and take phone pictures of each of the flies so the model would work well in the desired context. This took a while. I took around 100 photos of each class at all different angles, backgrounds, distances, etc. to try to give the CNN good variety. 

Now I was ready to train my model on both the internet pictures and the phone pictures. All images were center cropped to 256x256 pixels. My structure was a simple convolutional neural network built in Keras.

![modelStructure](https://github.com/SamHero16/FindAFly/assets/132628480/25316eb5-4fed-4b73-954a-7e3a97862a99)

This worked decently and had a respectable accuracy, but for this to have any standing I needed a model with very high accuracy.  I began to understand that 22 classes of very similar looking flies is hard for a network, given the limited amount of data and computation power I had. So, I came up with an alternative model with only 13 classes of the very most popular flies. This sacrificed the idea of ‘classifying any fly in your box,’ but greatly increased accuracy. I hoped to merge these two ideals, but don’t have the sufficient data or resources.  

Train, validation, and test sets contain images from google as well as phone images captured by me. After a lot of fiddling, I reached these metrics: 

Validation Loss: 0.188
Validation Accuracy: 0.969

Test Loss: 0.0612
Test Accuracy: 0.992

I created a small app to show this in action. The available pictures were set aside from the notebook entirely. 

https://github.com/SamHero16/FindAFly/assets/132628480/15ef36f6-6481-4823-b761-d0a52c50899b

Future work to be done:
- Run and document the 22-class model for comparison.
- Get more/better data.
- Make the app available on github (issues with uploading my huge Keras model.






