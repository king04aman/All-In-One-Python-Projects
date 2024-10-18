import requests
import json
import time
import os
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)

refs = [
    "/vserver/vserver_images.php",
    "/vserver/vps.php",
    "/vserver/",
    "/vserver/root-server-erweiterungen.php",
    "/",
    "/hosting",
    "/bestellen/domainangebote.php",
    "/bestellen/softwareangebote.php",
    "/ssl-zertifikate/",
    "/ueber-netcup/",
    "/ueber-netcup/hardware-infrastruktur.php",
    "/ueber-netcup/ddos-schutz-filter.php",
    "/ueber-netcup/auszeichnungen.php",
    "/ueber-netcup/zertifizierungen.php",
    "/ueber-netcup/partner.php",
    "/groupware/",
    "/professional/",
    "/professional/dedizierte-server/",
    "/professional/managed-server/",
    "/professional/colocation/",
    "/professional/softwareentwicklung/",
]

def get_price_formatted(price):
    return price.replace(",", ".").replace("€", "EUR").replace(" ", "")

def sanitize_filename(filename):
    return filename.replace("/", "_").replace("|", "_").replace("\\", "_").replace(":", "_").replace("*", "_").replace("?", "_").replace('"', "_").replace("<", "_").replace(">", "_")

def main():
    current_year = datetime.now().year
    folder_path = f"eggs_{current_year}"
    
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        
    while True:
        
        for r in refs:

            try:
                resp = requests.post("https://www.netcup.de/api/eggs", data={"requrl": r})
                response_text = json.loads(resp.text)["eggs"]
                if response_text is None or not response_text:
                    continue

                egg = response_text[0]
                if egg['title'][-1] == " ":
                    egg['title'] = egg['title'][:-1]
                
                price = get_price_formatted(egg["price"])
                file_name = sanitize_filename(f"{price}_{egg['id']}.json")
                sub_folder = sanitize_filename(f"{egg['title']}").replace(" ","_")
                
                full_folder_path = os.path.join(folder_path, sub_folder)
                if not os.path.exists(full_folder_path):
                    os.makedirs(full_folder_path)

                path = os.path.join(full_folder_path, file_name)
                
                egg['original_url'] = f"https://www.netcup.de/bestellen/produkt.php?produkt={egg['product_id']}&ref=230003&hiddenkey={egg['product_key']}"
                egg['found_url'] = f"https://www.netcup.de{r}"
                egg['found_unix_time'] = int(time.time())
                with open(path, "w") as file:
                    json.dump(egg, file, indent=4)

                logging.info(f"{'-' * 10}")
                logging.info(f"{egg['title']}")
                logging.info(f"{price}")
                logging.info(f"{egg['original_url']}")
                logging.info(f"{egg['found_url']}")
                logging.info(f"Found Unix Time: {egg['found_unix_time']}")
                logging.info(f"{'-' * 10}")
            
            except requests.exceptions.RequestException as e:
                logging.error(f"Request failed: {e}")
                continue
            except json.JSONDecodeError as e:
                logging.error(f"Failed to decode JSON: {e}")
                continue
            except Exception as e:
                logging.error(f"An unexpected error occurred: {e}")
                continue
        
        logging.info(f"\n\n Time Sleep - {2*60}")
        time.sleep(2 * 60)

if __name__ == "__main__":
    main()

