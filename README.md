 # LEAFIE

<img width="1678" height="895" alt="Screenshot 2026-10-11 201538" src="https://github.com/user-attachments/assets/dd25e9e6-da6c-4caa-82a2-ef61b1923e82" />


This is my Starbie-inspired PCB pet project --> LEAFIE!

LEAFIE is a tiny motion-controlled digital pet, created using Starbie's guide on GitHub. He too is also a pet that is controlled by motion rather than using controls.

## What is it?

It is a pet that sits on your desk, displays personality and character on the display, and can be interacted with via two buttons and a motion sensor. 
It includes a microcontroller, display, motion sensor, and environmental sensor in a custom-designed PCB in the shape of a Canadian maple leaf.

## How was it made?

I used the beginner [Starbie project](https://halflife.hackclub.com/) for the exact components and firmware. But I took creative liberties when designing the board itself. I decided to use a maple leaf, and I had to change up a few of the connections to make my PCB flow better.

<img width="1667" height="973" alt="image" src="https://github.com/user-attachments/assets/7c6fdf2c-3335-4c5c-ab27-c919dbdf705e" />


## Why was it designed this way?

I chose the PCB design to look like a maple leaf, and added Canadian-themed symbols all over the back and front to show my love for my country Canada. I am a proud Canadian and thought this was a very cool idea to showcase my spirit!

## Project status

Currently, PCB files are complete, and firmware is ready, waiting for the project to be approved and shipped in week 6 of half-life!

## Bill of Materials (BOM)

| Part | What it's for | Qty | Unit | Total | Vendor | Link |
| :--- | :--- | :---: | :---: | :---: | :--- | :--- |
| **DHT11 Digital Temp & Humidity Sensor Module** | Environmental Sensor For Pet | 1 | $2.31 | $2.31 | AliExpress | [View Link](https://www.aliexpress.com/item/1005001234567890.html) |
| **ESP 32 - C3 Mini** | For controlling the brain | 1 | $5.52 | $5.52 | AliExpress | [View Link](https://www.aliexpress.com/item/1005007890123456.html) |
| **Resistors** | Resistors for project | 1 | $1.19 | $1.19 | AliExpress | [View Link](https://www.aliexpress.com/item/1005003456789012.html) |
| **Switches** | For switches input to pet | 1 | $1.19 | $1.19 | AliExpress | [View Link](https://www.aliexpress.com/item/1005005678901234.html) |
| **MPU6050 Module 6 Axis IMU** | For the motion control | 1 | $1.66 | $1.66 | AliExpress | [View Link](https://www.aliexpress.com/item/1005006789012345.html) |
| **LEAFIE PCB** | PCB for project | 1 | $6.10 | $6.10 | JLCPCB | [View Link](https://jlcpcb.com) |

* **Parts Subtotal:** $17.97
* **Tax & Shipping:** $8.93
* **Total Estimated Cost:** **$26.90**

  
## Repository contents

- `PCB/` - KiCad source files and fabrication exports
- `Firmware/` - Arduino IDE starter sketch
