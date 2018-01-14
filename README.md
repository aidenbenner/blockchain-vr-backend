## Blockchain VR
The backend code for our VR Crypto visualization. This is the code that parses blocks and transactions into a useful format and saves it in a format to be read by the vr side. 
We used blockchain.info to fetch the most recent blocks by following the previous hash of each block. 
We clean the data sent to us and export it to json to be read by the unreal engine. We also needed to write the model classes for c++ in unreal. 

