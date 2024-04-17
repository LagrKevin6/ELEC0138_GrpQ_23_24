import pyshark

def extract_username(pcap_file):
    # Load the pcap file
    cap = pyshark.FileCapture(pcap_file, display_filter='http.request.method == "POST"')

    try:
        for packet in cap:
            print(packet.layers[-1])
    except:
        print('opening .pcapng file failed')
    cap.close()



file_path = 'username_leak.pcapng'
extract_username(file_path)

