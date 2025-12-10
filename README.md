# ZSOD
*uploaded only sample files as files are larger than 250MB*
zero shot object detection webapp
Zero-Shot Object Detection (ZSOD) is an emerging computer vision paradigm that enables the 
detection of novel object categories without requiring explicit training examples, using natural 
language descriptions as queries. While models such as Grounding DINO and Segment 
Anything Model (SAM) exhibit strong detection and segmentation capabilities, existing 
implementations are largely confined to research settings, often lack real-time performance, 
and remain inaccessible to non-technical users. This project proposes a web-based, real-time 
system that integrates Grounding DINO for prompt-based zero-shot detection, SAM for high
precision segmentation, and object tracking mechanisms to maintain object identities across 
video frames. Additionally, it incorporates scene understanding, generating descriptive 
captions and contextual relationships between objects. The system accepts free-form text 
prompts, identifies corresponding objects in static images or live webcam feeds, generates 
pixel-accurate masks, tracks objects across frames, and provides scene-level interpretations 
through a user-friendly interface with features like image upload, live detection, and one-click 
download of results. By combining state-of-the-art vision-language models and tracking 
mechanisms, the proposed approach addresses key deployment challenges, including latency, 
accuracy, scalability, and usability. Potential applications include surveillance, autonomous 
navigation, e-commerce product tagging, interactive educational tools, and rapid prototyping 
for AI-driven visual systems. This project demonstrates how zero-shot detection, segmentation, 
tracking, and scene understanding can be effectively integrated into a responsive, real-world 
platform, bridging the gap between research prototypes and practical AI solutions. 
Furthermore, the system emphasizes modularity and extensibility, allowing easy integration of 
emerging vision-language models as they evolve. It supports multi-object and multi-prompt 
queries, enabling complex scene analyses in dynamic environments. To ensure robustness, the 
architecture employs optimized model inference pipelines and GPU acceleration for real-time 
processing
