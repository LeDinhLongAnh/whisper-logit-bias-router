# Danh sách toàn bộ câu test gốc (đã loại trùng) và mức độ chính xác

Tổng hợp từ 3 file báo cáo (TEST_REPORT.md, TEST_REPORT_1.md, TEST_REPORT_2.md) — 726 lượt test gốc, **342 câu chuẩn duy nhất**.

Mỗi câu được tính trên toàn bộ các lần xuất hiện và cả 3 chế độ nhận dạng (Không Prompt, Global Prompt, Global + Logit Bias) — tổng cộng số lượt thử = số lần xuất hiện × 3 chế độ (trừ vài ô thiếu dữ liệu).

| STT | Câu test gốc | Số lần xuất hiện | Kết quả | WER trung bình |
|---:|---|:---:|---|:---:|
| 1 | Set an alarm for six thirty tomorrow morning. | 4 | ⚠️ Sai 12/12 lượt thử | 253.1% |
| 2 | Resume playback. | 2 | ⚠️ Sai 6/6 lượt thử | 150.0% |
| 3 | Call my brother. | 2 | ⚠️ Sai 6/6 lượt thử | 133.3% |
| 4 | Tell me the Wi-Fi throughput. | 2 | ⚠️ Sai 6/6 lượt thử | 110.0% |
| 5 | Play something upbeat. | 5 | ⚠️ Sai 11/15 lượt thử | 108.9% |
| 6 | Show me the router's operational status. | 2 | ⚠️ Sai 6/6 lượt thử | 105.6% |
| 7 | Is the guest network enabled? | 2 | ⚠️ Sai 6/6 lượt thử | 93.3% |
| 8 | Please disable guest network access. | 2 | ⚠️ Sai 6/6 lượt thử | 93.3% |
| 9 | Please measure the round-trip time. | 2 | ⚠️ Sai 6/6 lượt thử | 93.3% |
| 10 | Read my unread messages. | 2 | ⚠️ Sai 6/6 lượt thử | 91.7% |
| 11 | Cancel my alarm for tomorrow. | 2 | ⚠️ Sai 6/6 lượt thử | 86.7% |
| 12 | Is my Wi-Fi speed normal? | 2 | ⚠️ Sai 5/6 lượt thử | 86.7% |
| 13 | Mute the audio. | 2 | ⚠️ Sai 6/6 lượt thử | 83.4% |
| 14 | Turn the fan on. | 2 | ⚠️ Sai 6/6 lượt thử | 83.3% |
| 15 | Make the bedroom lights brighter. | 2 | ⚠️ Sai 6/6 lượt thử | 80.0% |
| 16 | Disable the guest Wi-Fi. | 2 | ⚠️ Sai 6/6 lượt thử | 75.0% |
| 17 | Stop playing this song. | 2 | ⚠️ Sai 6/6 lượt thử | 75.0% |
| 18 | Give me today's weather forecast. | 2 | ⚠️ Sai 6/6 lượt thử | 66.7% |
| 19 | Can you test the latency right now? | 2 | ⚠️ Sai 6/6 lượt thử | 64.2% |
| 20 | Show all currently connected clients. | 2 | ⚠️ Sai 5/6 lượt thử | 63.3% |
| 21 | Rename this device | 3 | ⚠️ Sai 8/9 lượt thử | 63.0% |
| 22 | Set a reminder to charge my laptop | 3 | ⚠️ Sai 9/9 lượt thử | 61.9% |
| 23 | Show me this device's network address. | 2 | ⚠️ Sai 6/6 lượt thử | 61.1% |
| 24 | What's my download speed right now? | 2 | ⚠️ Sai 6/6 lượt thử | 61.1% |
| 25 | What's today's date? | 4 | ⚠️ Sai 12/12 lượt thử | 61.1% |
| 26 | Give me the gateway details. | 2 | ⚠️ Sai 6/6 lượt thử | 60.0% |
| 27 | What's the router's current condition? | 2 | ⚠️ Sai 6/6 lượt thử | 60.0% |
| 28 | Do I need an umbrella today? | 2 | ⚠️ Sai 6/6 lượt thử | 58.4% |
| 29 | Play that track again. | 2 | ⚠️ Sai 6/6 lượt thử | 58.3% |
| 30 | Enable the guest Wi-Fi. | 2 | ⚠️ Sai 2/6 lượt thử | 58.3% |
| 31 | Check whether guest Wi-Fi is active. | 2 | ⚠️ Sai 6/6 lượt thử | 55.6% |
| 32 | Unmute the speaker. | 2 | ⚠️ Sai 6/6 lượt thử | 55.6% |
| 33 | List all gadgets connected to the home network. | 2 | ⚠️ Sai 6/6 lượt thử | 54.2% |
| 34 | Optimize gaming for the PC. | 4 | ⚠️ Sai 9/12 lượt thử | 53.3% |
| 35 | Is my network latency high? | 2 | ⚠️ Sai 6/6 lượt thử | 53.3% |
| 36 | Reboot my home gateway now. | 2 | ⚠️ Sai 4/6 lượt thử | 53.3% |
| 37 | Enable the guest wireless network. | 2 | ⚠️ Sai 2/6 lượt thử | 53.3% |
| 38 | Please tell me the default gateway. | 2 | ⚠️ Sai 6/6 lượt thử | 52.8% |
| 39 | Check for firmware updates. | 4 | ⚠️ Sai 12/12 lượt thử | 52.1% |
| 40 | Run a speed test. | 6 | ⚠️ Sai 13/15 lượt thử | 51.7% |
| 41 | Allow internet only from 6 AM to 8 PM on my son's device. | 3 | ⚠️ Sai 9/9 lượt thử | 51.3% |
| 42 | Cancel my grocery reminder. | 2 | ⚠️ Sai 6/6 lượt thử | 50.0% |
| 43 | Give me the network details for my laptop. | 2 | ⚠️ Sai 6/6 lượt thử | 50.0% |
| 44 | Move my meeting to four thirty. | 2 | ⚠️ Sai 6/6 lượt thử | 50.0% |
| 45 | Schedule a call for two o'clock. | 2 | ⚠️ Sai 6/6 lượt thử | 50.0% |
| 46 | Show me every device connected to the router. | 2 | ⚠️ Sai 6/6 lượt thử | 50.0% |
| 47 | Skip to the next song. | 2 | ⚠️ Sai 6/6 lượt thử | 50.0% |
| 48 | Is guest Wi-Fi currently turned on? | 2 | ⚠️ Sai 2/6 lượt thử | 50.0% |
| 49 | Who is video call right now? | 5 | ⚠️ Sai 15/15 lượt thử | 47.8% |
| 50 | Show the current network status. | 2 | ⚠️ Sai 6/6 lượt thử | 46.7% |
| 51 | What's the router's IP address? | 2 | ⚠️ Sai 6/6 lượt thử | 46.7% |
| 52 | Give me today's weather forecast | 1 | ⚠️ Sai 3/3 lượt thử | 46.7% |
| 53 | Block YouTube for the tablet. | 2 | ⚠️ Sai 2/6 lượt thử | 46.7% |
| 54 | Am I connected to the home Wi-Fi? | 2 | ⚠️ Sai 5/6 lượt thử | 45.2% |
| 55 | Show device info for the tablet. | 2 | ⚠️ Sai 6/6 lượt thử | 44.5% |
| 56 | Is the ping stable right now? | 2 | ⚠️ Sai 4/6 lượt thử | 44.5% |
| 57 | Show me nearby places to eat. | 2 | ⚠️ Sai 6/6 lượt thử | 44.4% |
| 58 | Tell me when it's noon. | 3 | ⚠️ Sai 9/9 lượt thử | 44.4% |
| 59 | Will it rain later today? | 5 | ⚠️ Sai 15/15 lượt thử | 44.0% |
| 60 | Disable internet access on the guest laptop. | 2 | ⚠️ Sai 6/6 lượt thử | 42.9% |
| 61 | Show the signal bars for this device. | 2 | ⚠️ Sai 6/6 lượt thử | 42.9% |
| 62 | Show my upcoming reminders. | 3 | ⚠️ Sai 9/9 lượt thử | 41.7% |
| 63 | Tell me the network information for this client. | 2 | ⚠️ Sai 5/6 lượt thử | 41.7% |
| 64 | enable the guest Wi-Fi | 2 | ⚠️ Sai 3/6 lượt thử | 41.7% |
| 65 | Rename my Wi-Fi network. | 2 | ⚠️ Sai 2/6 lượt thử | 41.7% |
| 66 | Who sent me a message? | 2 | ⚠️ Sai 6/6 lượt thử | 40.0% |
| 67 | Is my Wi-Fi coverage good in this spot? | 2 | ⚠️ Sai 6/6 lượt thử | 39.6% |
| 68 | Dial the last number I called. | 2 | ⚠️ Sai 6/6 lượt thử | 38.9% |
| 69 | How's the response time on my network? | 2 | ⚠️ Sai 6/6 lượt thử | 38.1% |
| 70 | What's the ping time to the internet? | 2 | ⚠️ Sai 6/6 lượt thử | 38.1% |
| 71 | Check the status of the guest network. | 2 | ⚠️ Sai 6/6 lượt thử | 38.1% |
| 72 | Is my router running the latest firmware? | 2 | ⚠️ Sai 4/6 lượt thử | 38.1% |
| 73 | Tell me my network's default gateway address. | 2 | ⚠️ Sai 2/6 lượt thử | 38.1% |
| 74 | Disable internet access on the guest laptop | 1 | ⚠️ Sai 1/3 lượt thử | 38.1% |
| 75 | Check the router status. | 4 | ⚠️ Sai 8/12 lượt thử | 37.5% |
| 76 | Can you list who's online on my Wi-Fi? | 2 | ⚠️ Sai 6/6 lượt thử | 37.5% |
| 77 | Please run a speed test on the Wi-Fi. | 2 | ⚠️ Sai 6/6 lượt thử | 37.5% |
| 78 | Turn on my desk lamp. | 2 | ⚠️ Sai 6/6 lượt thử | 36.7% |
| 79 | Create a weekday alarm at seven. | 5 | ⚠️ Sai 15/15 lượt thử | 36.7% |
| 80 | Has my phone joined the Wi-Fi network? | 2 | ⚠️ Sai 6/6 lượt thử | 35.8% |
| 81 | What connection details does my phone have? | 2 | ⚠️ Sai 5/6 lượt thử | 35.8% |
| 82 | Can you confirm whether the internet is online? | 2 | ⚠️ Sai 6/6 lượt thử | 35.4% |
| 83 | Tell me which devices are using the network. | 2 | ⚠️ Sai 5/6 lượt thử | 35.4% |
| 84 | Can you power cycle the router? | 2 | ⚠️ Sai 6/6 lượt thử | 33.4% |
| 85 | Is there heavy traffic on my route? | 2 | ⚠️ Sai 6/6 lượt thử | 33.4% |
| 86 | What reminders do I have today? | 2 | ⚠️ Sai 3/6 lượt thử | 33.4% |
| 87 | Can you pull up my laptop's Wi-Fi details? | 2 | ⚠️ Sai 6/6 lượt thử | 33.3% |
| 88 | Is my laptop currently connected to Wi-Fi? | 2 | ⚠️ Sai 6/6 lượt thử | 33.3% |
| 89 | Is my smart TV connected to the network? | 2 | ⚠️ Sai 6/6 lượt thử | 33.3% |
| 90 | Is the WAN connection working? | 2 | ⚠️ Sai 6/6 lượt thử | 33.3% |
| 91 | Let the laptop connect to the internet | 2 | ⚠️ Sai 5/6 lượt thử | 33.3% |
| 92 | How is the network today? | 3 | ⚠️ Sai 3/9 lượt thử | 33.3% |
| 93 | Read my latest message. | 2 | ⚠️ Sai 2/6 lượt thử | 33.3% |
| 94 | Show me the guest Wi-Fi status. | 2 | ⚠️ Sai 2/6 lượt thử | 33.3% |
| 95 | Is the Wi-Fi signal weak here? | 2 | ⚠️ Sai 5/6 lượt thử | 33.3% |
| 96 | Pause the music. | 2 | ⚠️ Sai 6/6 lượt thử | 33.3% |
| 97 | Show the active devices on Wi-Fi. | 2 | ⚠️ Sai 6/6 lượt thử | 33.3% |
| 98 | Wake me up at 7 AM. | 2 | ⚠️ Sai 6/6 lượt thử | 33.3% |
| 99 | Wake me up at seven fifteen. | 2 | ⚠️ Sai 6/6 lượt thử | 33.3% |
| 100 | Please check if this laptop is on Wi-Fi. | 2 | ⚠️ Sai 6/6 lượt thử | 31.2% |
| 101 | Send a text saying I'll be late. | 2 | ⚠️ Sai 6/6 lượt thử | 31.0% |
| 102 | Cancel the meeting at three. | 2 | ⚠️ Sai 5/6 lượt thử | 30.0% |
| 103 | Show me all devices that are online. | 2 | ⚠️ Sai 6/6 lượt thử | 28.6% |
| 104 | Remind me when the alarm goes off. | 3 | ⚠️ Sai 8/9 lượt thử | 28.6% |
| 105 | Can you check the router health? | 2 | ⚠️ Sai 6/6 lượt thử | 27.8% |
| 106 | Can you power cycle the router | 1 | ⚠️ Sai 3/3 lượt thử | 27.8% |
| 107 | Show me my schedule for tomorrow. | 2 | ⚠️ Sai 6/6 lượt thử | 27.8% |
| 108 | Show the current Wi-Fi signal level. | 2 | ⚠️ Sai 6/6 lượt thử | 27.8% |
| 109 | Restore Wi-Fi access to my phone. | 3 | ⚠️ Sai 3/9 lượt thử | 27.8% |
| 110 | Is the guest access currently active? | 2 | ⚠️ Sai 2/6 lượt thử | 27.8% |
| 111 | What time is it and what's the weather today? | 4 | ⚠️ Sai 12/12 lượt thử | 26.8% |
| 112 | Please display the gateway settings. | 2 | ⚠️ Sai 6/6 lượt thử | 26.7% |
| 113 | Show the local router address. | 2 | ⚠️ Sai 2/6 lượt thử | 26.7% |
| 114 | Move my alarm to half past six. | 2 | ⚠️ Sai 6/6 lượt thử | 26.2% |
| 115 | Lock the front door. | 2 | ⚠️ Sai 6/6 lượt thử | 25.0% |
| 116 | Set the room temperature to twenty two degrees. | 2 | ⚠️ Sai 6/6 lượt thử | 25.0% |
| 117 | What do I have on my calendar today? | 2 | ⚠️ Sai 6/6 lượt thử | 25.0% |
| 118 | Who's currently connected to the Wi-Fi? | 2 | ⚠️ Sai 6/6 lượt thử | 25.0% |
| 119 | Update the router software. | 2 | ⚠️ Sai 2/6 lượt thử | 25.0% |
| 120 | Prevent gaming on the laptop. | 3 | ⚠️ Sai 3/9 lượt thử | 24.4% |
| 121 | Is there a lot of lag on my connection? | 2 | ⚠️ Sai 6/6 lượt thử | 24.0% |
| 122 | Do I have any meetings this afternoon? | 2 | ⚠️ Sai 6/6 lượt thử | 23.8% |
| 123 | Is my internet speed slower than usual? | 2 | ⚠️ Sai 6/6 lượt thử | 23.8% |
| 124 | What's the MAC address of this device? | 2 | ⚠️ Sai 6/6 lượt thử | 23.8% |
| 125 | Please show the current data transfer speed. | 2 | ⚠️ Sai 5/6 lượt thử | 23.8% |
| 126 | Reset the password for the guest network. | 2 | ⚠️ Sai 2/6 lượt thử | 23.8% |
| 127 | Turn off the guest Wi-Fi for me. | 2 | ⚠️ Sai 2/6 lượt thử | 23.8% |
| 128 | Please turn the guest Wi-Fi on | 3 | ⚠️ Sai 8/9 lượt thử | 22.2% |
| 129 | Please list all clients on the network right now. | 2 | ⚠️ Sai 6/6 lượt thử | 22.2% |
| 130 | Please show all devices using the internet right now. | 2 | ⚠️ Sai 6/6 lượt thử | 22.2% |
| 131 | Check the network gateway information. | 2 | ⚠️ Sai 6/6 lượt thử | 20.0% |
| 132 | Start playing my favorite playlist. | 2 | ⚠️ Sai 6/6 lượt thử | 20.0% |
| 133 | Send a message to Sarah. | 2 | ⚠️ Sai 4/6 lượt thử | 20.0% |
| 134 | Show me the current ping. | 2 | ⚠️ Sai 4/6 lượt thử | 20.0% |
| 135 | How fast is my wireless connection? | 2 | ⚠️ Sai 5/6 lượt thử | 19.4% |
| 136 | Check if my laptop is connected to the router. | 2 | ⚠️ Sai 6/6 lượt thử | 18.5% |
| 137 | Can you show the IP address of my phone? | 2 | ⚠️ Sai 5/6 lượt thử | 18.5% |
| 138 | List the devices currently using Wi-Fi. | 4 | ⚠️ Sai 12/12 lượt thử | 16.7% |
| 139 | Can you check my wireless signal? | 2 | ⚠️ Sai 6/6 lượt thử | 16.7% |
| 140 | Do we currently have internet access? | 2 | ⚠️ Sai 6/6 lượt thử | 16.7% |
| 141 | Is my connection responsive or laggy? | 2 | ⚠️ Sai 6/6 lượt thử | 16.7% |
| 142 | Please confirm the router is online. | 2 | ⚠️ Sai 6/6 lượt thử | 16.7% |
| 143 | Set a morning alarm for eight. | 2 | ⚠️ Sai 6/6 lượt thử | 16.7% |
| 144 | Show the current default route information. | 2 | ⚠️ Sai 6/6 lượt thử | 16.7% |
| 145 | What's the weather like this morning? | 2 | ⚠️ Sai 6/6 lượt thử | 16.7% |
| 146 | Show my gateway information. | 4 | ⚠️ Sai 8/12 lượt thử | 16.7% |
| 147 | When is my next meeting? | 2 | ⚠️ Sai 5/6 lượt thử | 16.7% |
| 148 | Find a restaurant nearby. | 2 | ⚠️ Sai 4/6 lượt thử | 16.7% |
| 149 | Start a relaxing playlist. | 2 | ⚠️ Sai 4/6 lượt thử | 16.7% |
| 150 | Add a meeting for Friday morning. | 2 | ⚠️ Sai 2/6 lượt thử | 16.7% |
| 151 | Is the Wi-Fi stable? | 2 | ⚠️ Sai 2/6 lượt thử | 16.7% |
| 152 | What is the current Wi-Fi name? | 2 | ⚠️ Sai 2/6 lượt thử | 16.7% |
| 153 | Is this device hooked up to the wireless network? | 2 | ⚠️ Sai 6/6 lượt thử | 14.8% |
| 154 | Is my device connected to the home network? | 2 | ⚠️ Sai 6/6 lượt thử | 14.6% |
| 155 | Check whether the router is operating normally. | 2 | ⚠️ Sai 6/6 lượt thử | 14.3% |
| 156 | Please tell me the wireless signal level. | 2 | ⚠️ Sai 6/6 lượt thử | 14.3% |
| 157 | Start the last playlist I listened to. | 2 | ⚠️ Sai 6/6 lượt thử | 14.3% |
| 158 | Turn off the alarm I just set. | 2 | ⚠️ Sai 6/6 lượt thử | 14.3% |
| 159 | How's the wireless signal in this room? | 2 | ⚠️ Sai 4/6 lượt thử | 14.3% |
| 160 | Can you show the router gateway IP? | 2 | ⚠️ Sai 3/6 lượt thử | 14.3% |
| 161 | What will the weather be like tomorrow? | 3 | ⚠️ Sai 6/9 lượt thử | 14.3% |
| 162 | Test the Wi-Fi speed on my laptop. | 2 | ⚠️ Sai 2/6 lượt thử | 14.3% |
| 163 | What is my router's local IP address? | 2 | ⚠️ Sai 2/6 lượt thử | 14.3% |
| 164 | Get the connection details for my phone. | 3 | ⚠️ Sai 4/9 lượt thử | 14.3% |
| 165 | Create a reminder for eight tonight. | 2 | ⚠️ Sai 5/6 lượt thử | 13.9% |
| 166 | Lower the thermostat by two degrees. | 2 | ⚠️ Sai 5/6 lượt thử | 13.9% |
| 167 | Play something I listened to yesterday. | 2 | ⚠️ Sai 5/6 lượt thử | 13.9% |
| 168 | Set the lights to fifty percent. | 2 | ⚠️ Sai 5/6 lượt thử | 13.9% |
| 169 | What is my first appointment today? | 2 | ⚠️ Sai 5/6 lượt thử | 13.9% |
| 170 | Show my phone's network configuration. | 2 | ⚠️ Sai 4/6 lượt thử | 13.3% |
| 171 | Is the broadband connection working? | 2 | ⚠️ Sai 2/6 lượt thử | 13.3% |
| 172 | Is the router working normally? | 2 | ⚠️ Sai 2/6 lượt thử | 13.3% |
| 173 | Switch off the bedroom light. | 2 | ⚠️ Sai 2/6 lượt thử | 13.3% |
| 174 | Can you check the gateway address for me? | 2 | ⚠️ Sai 6/6 lượt thử | 12.5% |
| 175 | Can you verify the WAN link is up? | 2 | ⚠️ Sai 6/6 lượt thử | 12.5% |
| 176 | Tell me whether this device is on Wi-Fi. | 2 | ⚠️ Sai 6/6 lượt thử | 12.5% |
| 177 | What time will it be in thirty minutes? | 2 | ⚠️ Sai 6/6 lượt thử | 12.5% |
| 178 | Who is connected to my router right now? | 2 | ⚠️ Sai 6/6 lượt thử | 12.5% |
| 179 | Please show the Wi-Fi info for my smartphone. | 2 | ⚠️ Sai 3/6 lượt thử | 12.5% |
| 180 | Can you give me a router health check? | 2 | ⚠️ Sai 2/6 lượt thử | 12.5% |
| 181 | Can you give me the time in Tokyo? | 2 | ⚠️ Sai 2/6 lượt thử | 12.5% |
| 182 | Can you show the current wireless reception? | 2 | ⚠️ Sai 5/6 lượt thử | 11.9% |
| 183 | How do I get to the office? | 2 | ⚠️ Sai 5/6 lượt thử | 11.9% |
| 184 | Remind me about the appointment at three. | 2 | ⚠️ Sai 5/6 lượt thử | 11.9% |
| 185 | Tell me the forecast for this weekend. | 2 | ⚠️ Sai 5/6 lượt thử | 11.9% |
| 186 | How good is the Wi-Fi coverage? | 2 | ⚠️ Sai 2/6 lượt thử | 11.1% |
| 187 | Limit the phone to 50 Mbps. | 2 | ⚠️ Sai 2/6 lượt thử | 11.1% |
| 188 | Show device information for my phone. | 2 | ⚠️ Sai 2/6 lượt thử | 11.1% |
| 189 | Show me the router's internal address. | 2 | ⚠️ Sai 2/6 lượt thử | 11.1% |
| 190 | What gateway is this device using? | 2 | ⚠️ Sai 2/6 lượt thử | 11.1% |
| 191 | Which devices are connected right now? | 2 | ⚠️ Sai 2/6 lượt thử | 11.1% |
| 192 | Give me the connection details for my tablet. | 2 | ⚠️ Sai 5/6 lượt thử | 10.4% |
| 193 | Turn on the lights and Turn off the TV. | 4 | ⚠️ Sai 9/12 lượt thử | 10.2% |
| 194 | Can you measure the network response time? | 2 | ⚠️ Sai 2/6 lượt thử | 9.5% |
| 195 | Check if the network delay is high. | 2 | ⚠️ Sai 2/6 lượt thử | 9.5% |
| 196 | How's my Wi-Fi reception at the moment? | 2 | ⚠️ Sai 2/6 lượt thử | 9.5% |
| 197 | Please check the ping to my router. | 2 | ⚠️ Sai 2/6 lượt thử | 9.5% |
| 198 | Show the default route for my network. | 2 | ⚠️ Sai 2/6 lượt thử | 9.5% |
| 199 | What's the Wi-Fi signal quality right now? | 2 | ⚠️ Sai 2/6 lượt thử | 9.5% |
| 200 | What address does my router use as gateway? | 2 | ⚠️ Sai 4/6 lượt thử | 8.3% |
| 201 | Check my Wi-Fi speed. | 2 | ⚠️ Sai 2/6 lượt thử | 8.3% |
| 202 | Check the Wi-Fi reception. | 2 | ⚠️ Sai 2/6 lượt thử | 8.3% |
| 203 | Check the connection delay. | 2 | ⚠️ Sai 2/6 lượt thử | 8.3% |
| 204 | How long will it take to get downtown? | 2 | ⚠️ Sai 2/6 lượt thử | 8.3% |
| 205 | Please check if there's an active internet connection. | 2 | ⚠️ Sai 2/6 lượt thử | 8.3% |
| 206 | Is my phone connected to the Wi-Fi right now? | 2 | ⚠️ Sai 4/6 lượt thử | 7.4% |
| 207 | What are the IP and status of the laptop? | 2 | ⚠️ Sai 4/6 lượt thử | 7.4% |
| 208 | How many days are left this month? | 2 | ⚠️ Sai 3/6 lượt thử | 7.2% |
| 209 | Is there an internet outage right now? | 2 | ⚠️ Sai 3/6 lượt thử | 7.2% |
| 210 | Turn the guest network on for visitors. | 2 | ⚠️ Sai 3/6 lượt thử | 7.2% |
| 211 | Boost YouTube on my laptop. | 2 | ⚠️ Sai 2/6 lượt thử | 6.7% |
| 212 | Can you activate guest Wi-Fi? | 2 | ⚠️ Sai 2/6 lượt thử | 6.7% |
| 213 | Check the internet connection quality. | 2 | ⚠️ Sai 2/6 lượt thử | 6.7% |
| 214 | Hang up the current call. | 2 | ⚠️ Sai 2/6 lượt thử | 6.7% |
| 215 | Please deactivate the guest Wi-Fi. | 2 | ⚠️ Sai 2/6 lượt thử | 6.7% |
| 216 | Turn on the guest network. | 2 | ⚠️ Sai 2/6 lượt thử | 6.7% |
| 217 | What's the current network delay? | 2 | ⚠️ Sai 1/6 lượt thử | 6.7% |
| 218 | Does my laptop have an active Wi-Fi connection? | 2 | ⚠️ Sai 3/6 lượt thử | 6.2% |
| 219 | What is the quickest way to the airport? | 2 | ⚠️ Sai 3/6 lượt thử | 6.2% |
| 220 | Can you check my internet connection? | 2 | ⚠️ Sai 2/6 lượt thử | 5.6% |
| 221 | Check the download speed on Wi-Fi. | 2 | ⚠️ Sai 2/6 lượt thử | 5.6% |
| 222 | How fast is my broadband connection? | 2 | ⚠️ Sai 2/6 lượt thử | 5.6% |
| 223 | Is everything okay with the router? | 2 | ⚠️ Sai 2/6 lượt thử | 5.6% |
| 224 | What time is my next alarm? | 2 | ⚠️ Sai 2/6 lượt thử | 5.6% |
| 225 | Can you switch on the guest wireless? | 2 | ⚠️ Sai 2/6 lượt thử | 4.8% |
| 226 | Please check if the WAN is connected. | 2 | ⚠️ Sai 2/6 lượt thử | 4.8% |
| 227 | Show the MAC address of my laptop. | 2 | ⚠️ Sai 2/6 lượt thử | 4.8% |
| 228 | Show the network settings for this client. | 2 | ⚠️ Sai 2/6 lượt thử | 4.8% |
| 229 | Can you check whether the WAN is online? | 2 | ⚠️ Sai 2/6 lượt thử | 4.2% |
| 230 | Is my home network connected to the internet? | 2 | ⚠️ Sai 2/6 lượt thử | 4.2% |
| 231 | Is the wireless connection active on my computer? | 2 | ⚠️ Sai 2/6 lượt thử | 4.2% |
| 232 | Please check if the router is functioning properly. | 2 | ⚠️ Sai 2/6 lượt thử | 4.2% |
| 233 | What is the current status of my router? | 2 | ⚠️ Sai 2/6 lượt thử | 4.2% |
| 234 | Which clients are active on the network now? | 2 | ⚠️ Sai 2/6 lượt thử | 4.2% |
| 235 | Is my network able to reach the internet? | 2 | ⚠️ Sai 1/6 lượt thử | 4.2% |
| 236 | Why is the Wi-Fi so slow on my phone today? | 2 | ⚠️ Sai 2/6 lượt thử | 3.3% |
| 237 | Set a reminder to charge my laptop. | 2 | ⚠️ Sai 1/6 lượt thử | 2.4% |
| 238 | Give me directions to the nearest gas station. | 2 | ⚠️ Sai 1/6 lượt thử | 2.1% |
| 239 | Answer the incoming call. | 2 | ✅ Đúng 100% | 0.0% |
| 240 | Call my most recent contact. | 2 | ✅ Đúng 100% | 0.0% |
| 241 | Can you check the upload speed? | 2 | ✅ Đúng 100% | 0.0% |
| 242 | Can you check whether my laptop is connected to Wi-Fi? | 2 | ✅ Đúng 100% | 0.0% |
| 243 | Can you confirm my computer is linked to the router? | 2 | ✅ Đúng 100% | 0.0% |
| 244 | Can you display the IP address for my laptop? | 2 | ✅ Đúng 100% | 0.0% |
| 245 | Can you display the active connections on Wi-Fi? | 2 | ✅ Đúng 100% | 0.0% |
| 246 | Can you enable guest access? | 2 | ✅ Đúng 100% | 0.0% |
| 247 | Can you list the devices on my network? | 2 | ✅ Đúng 100% | 0.0% |
| 248 | Can you measure my Wi-Fi bandwidth? | 2 | ✅ Đúng 100% | 0.0% |
| 249 | Can you measure the current network speed? | 2 | ✅ Đúng 100% | 0.0% |
| 250 | Can you see if my tablet is connected to Wi-Fi? | 2 | ✅ Đúng 100% | 0.0% |
| 251 | Can you show me the gateway configuration? | 2 | ✅ Đúng 100% | 0.0% |
| 252 | Can you show me the router status? | 2 | ✅ Đúng 100% | 0.0% |
| 253 | Can you tell me the current latency? | 2 | ✅ Đúng 100% | 0.0% |
| 254 | Can you test the network speed? | 2 | ✅ Đúng 100% | 0.0% |
| 255 | Can you test the ping to the internet? | 2 | ✅ Đúng 100% | 0.0% |
| 256 | Can you verify my phone's Wi-Fi connection? | 2 | ✅ Đúng 100% | 0.0% |
| 257 | Can you verify the router is up and running? | 2 | ✅ Đúng 100% | 0.0% |
| 258 | Check how strong the wireless connection is. | 2 | ✅ Đúng 100% | 0.0% |
| 259 | Check if my smartphone is linked to the router. | 2 | ✅ Đúng 100% | 0.0% |
| 260 | Check if the router has internet access at the moment. | 2 | ✅ Đúng 100% | 0.0% |
| 261 | Check if the router is operating without issues. | 2 | ✅ Đúng 100% | 0.0% |
| 262 | Check the Wi-Fi connection on this device. | 2 | ✅ Đúng 100% | 0.0% |
| 263 | Check the connection speed on my device. | 2 | ✅ Đúng 100% | 0.0% |
| 264 | Check the network latency. | 2 | ✅ Đúng 100% | 0.0% |
| 265 | Check the upload speed on my network. | 2 | ✅ Đúng 100% | 0.0% |
| 266 | Check the wireless signal strength. | 2 | ✅ Đúng 100% | 0.0% |
| 267 | Check whether my router has internet access. | 2 | ✅ Đúng 100% | 0.0% |
| 268 | Check whether the connection has high delay. | 2 | ✅ Đúng 100% | 0.0% |
| 269 | Do I need an umbrella today | 1 | ✅ Đúng 100% | 0.0% |
| 270 | Does the network have an active internet connection? | 2 | ✅ Đúng 100% | 0.0% |
| 271 | Find a coffee shop near me. | 2 | ✅ Đúng 100% | 0.0% |
| 272 | Find the fastest route home. | 2 | ✅ Đúng 100% | 0.0% |
| 273 | Give me a status update for the router. | 2 | ✅ Đúng 100% | 0.0% |
| 274 | Give me the client details for my phone. | 2 | ✅ Đúng 100% | 0.0% |
| 275 | Go back to the previous track. | 2 | ✅ Đúng 100% | 0.0% |
| 276 | How cold is it outside right now? | 2 | ✅ Đúng 100% | 0.0% |
| 277 | How fast is the internet connection? | 2 | ✅ Đúng 100% | 0.0% |
| 278 | How hot will it be this afternoon? | 2 | ✅ Đúng 100% | 0.0% |
| 279 | How is the router doing right now? | 2 | ✅ Đúng 100% | 0.0% |
| 280 | How much latency does this network have? | 2 | ✅ Đúng 100% | 0.0% |
| 281 | How strong is the Wi-Fi signal? | 2 | ✅ Đúng 100% | 0.0% |
| 282 | Increase the volume a little. | 2 | ✅ Đúng 100% | 0.0% |
| 283 | Is it going to be sunny tomorrow? | 2 | ✅ Đúng 100% | 0.0% |
| 284 | Is my tablet on the wireless network at the moment? | 2 | ✅ Đúng 100% | 0.0% |
| 285 | Is the internet down right now? | 2 | ✅ Đúng 100% | 0.0% |
| 286 | Is the internet working right now? | 2 | ✅ Đúng 100% | 0.0% |
| 287 | Is the router connected to the internet | 2 | ✅ Đúng 100% | 0.0% |
| 288 | Is the router connected to the internet? | 2 | ✅ Đúng 100% | 0.0% |
| 289 | Is the router in good working order? | 2 | ✅ Đúng 100% | 0.0% |
| 290 | Is the router running fine at the moment? | 2 | ✅ Đúng 100% | 0.0% |
| 291 | Is the signal weak in this area? | 2 | ✅ Đúng 100% | 0.0% |
| 292 | Is the wireless signal strong enough? | 2 | ✅ Đúng 100% | 0.0% |
| 293 | Is there any rain expected tonight? | 2 | ✅ Đúng 100% | 0.0% |
| 294 | Is this computer connected to the wireless network? | 2 | ✅ Đúng 100% | 0.0% |
| 295 | List everything connected to the home network. | 2 | ✅ Đúng 100% | 0.0% |
| 296 | Open the curtains. | 2 | ✅ Đúng 100% | 0.0% |
| 297 | Play music from my library. | 2 | ✅ Đúng 100% | 0.0% |
| 298 | Play some instrumental music. | 2 | ✅ Đúng 100% | 0.0% |
| 299 | Play some relaxing music. | 2 | ✅ Đúng 100% | 0.0% |
| 300 | Please check the Wi-Fi strength here. | 2 | ✅ Đúng 100% | 0.0% |
| 301 | Please test my current internet speed. | 2 | ✅ Đúng 100% | 0.0% |
| 302 | Please turn on the guest network. | 2 | ✅ Đúng 100% | 0.0% |
| 303 | Put on a playlist for driving. | 2 | ✅ Đúng 100% | 0.0% |
| 304 | Put on some music for studying. | 2 | ✅ Đúng 100% | 0.0% |
| 305 | Remind me to buy coffee on the way home. | 2 | ✅ Đúng 100% | 0.0% |
| 306 | Remind me to call my manager this afternoon. | 2 | ✅ Đúng 100% | 0.0% |
| 307 | Remind me to send the report tomorrow morning. | 2 | ✅ Đúng 100% | 0.0% |
| 308 | Restart the router. | 2 | ✅ Đúng 100% | 0.0% |
| 309 | Set a reminder for my meeting tomorrow. | 2 | ✅ Đúng 100% | 0.0% |
| 310 | Set an alarm for ten minutes from now. | 2 | ✅ Đúng 100% | 0.0% |
| 311 | Show me the current connection speed. | 2 | ✅ Đúng 100% | 0.0% |
| 312 | Show my appointments for this week. | 2 | ✅ Đúng 100% | 0.0% |
| 313 | Show the connection information for my tablet. | 2 | ✅ Đúng 100% | 0.0% |
| 314 | Show the details of the selected device. | 2 | ✅ Đúng 100% | 0.0% |
| 315 | Show the devices currently online on my router. | 2 | ✅ Đúng 100% | 0.0% |
| 316 | Switch off guest access. | 2 | ✅ Đúng 100% | 0.0% |
| 317 | Take me to the nearest supermarket. | 2 | ✅ Đúng 100% | 0.0% |
| 318 | Tell me if the internet is available. | 2 | ✅ Đúng 100% | 0.0% |
| 319 | Tell me if the router is online. | 2 | ✅ Đúng 100% | 0.0% |
| 320 | Tell me the current gateway address. | 2 | ✅ Đúng 100% | 0.0% |
| 321 | Tell me the current time. | 2 | ✅ Đúng 100% | 0.0% |
| 322 | Tell me the signal strength for this device. | 2 | ✅ Đúng 100% | 0.0% |
| 323 | Turn off the air conditioner. | 2 | ✅ Đúng 100% | 0.0% |
| 324 | Turn off the guest network. | 2 | ✅ Đúng 100% | 0.0% |
| 325 | Turn the volume down. | 2 | ✅ Đúng 100% | 0.0% |
| 326 | What IP address is this device using? | 2 | ✅ Đúng 100% | 0.0% |
| 327 | What are the Wi-Fi details for this device? | 2 | ✅ Đúng 100% | 0.0% |
| 328 | What connection info is available for my tablet? | 2 | ✅ Đúng 100% | 0.0% |
| 329 | What day is it today? | 2 | ✅ Đúng 100% | 0.0% |
| 330 | What day of the week is it? | 2 | ✅ Đúng 100% | 0.0% |
| 331 | What devices are currently linked to the network? | 2 | ✅ Đúng 100% | 0.0% |
| 332 | What devices are online at the moment? | 2 | ✅ Đúng 100% | 0.0% |
| 333 | What is the current ping time? | 2 | ✅ Đúng 100% | 0.0% |
| 334 | What is the current signal quality? | 2 | ✅ Đúng 100% | 0.0% |
| 335 | What is the default gateway address? | 2 | ✅ Đúng 100% | 0.0% |
| 336 | What is the local IP of the router? | 2 | ✅ Đúng 100% | 0.0% |
| 337 | What is the router uptime? | 2 | ✅ Đúng 100% | 0.0% |
| 338 | What time is it right now? | 2 | ✅ Đúng 100% | 0.0% |
| 339 | What's the current network throughput? | 2 | ✅ Đúng 100% | 0.0% |
| 340 | What's the current time in London? | 2 | ✅ Đúng 100% | 0.0% |
| 341 | Why am I not getting internet access? | 2 | ✅ Đúng 100% | 0.0% |
| 342 | speed test | 2 | ✅ Đúng 100% | 0.0% |