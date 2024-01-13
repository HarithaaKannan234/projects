import streamlit as st
import pandas as pd
from streamlit_folium import folium_static

import folium




file_path = "C:\\Users\\Admin\\Desktop\\Murdoch\\pranav\\wetlands.csv"
df = pd.read_csv(file_path, encoding='latin1')
tab1, tab2 = st.tabs(["About", "Explore Wetlands"])



with tab2:

    
    def create_map(df):
        tamilnadu_map = folium.Map(location=[11.1271, 78.6569], zoom_start=8)

        for index, row in df.iterrows():
            # Add a marker for each wetland
            folium.Marker(
                location=[row['lat'], row['long']],
                tooltip=row['wet_lnd_name']
            ).add_to(tamilnadu_map)

        return tamilnadu_map
    
    
    st.title("Tamil Nadu Wetlands Map")
    wetlands_map = create_map(df)
    folium_static(wetlands_map)



    
    
    selected_wetland = st.selectbox("Select a wetland to view details:", df['wet_lnd_name'])
    
    if selected_wetland:
            selected_row = df[df['wet_lnd_name'] == selected_wetland].iloc[0]
            st.write(f"Location: {selected_row['wet_lnd_area']} ")
            st.write(f"Hectares: {selected_row['wet_lnd_acre']} Ha")
            st.write(f"Type: {selected_row['Type']} ")

            
            if selected_wetland == "Chitrangudi Bird Sanctuary":
                st.title("Chitrangudi Bird Sanctuary Overview")
                st.write("Chitrangudi Bird Sanctuary, nestled in the Ramanathapuram district of Tamil Nadu, is a sanctuary of immense ecological significance. Located approximately 15 kilometers from the Gulf of Mannar, this avian haven boasts a rich biodiversity amidst its diverse landscape. From seasonal freshwater tanks to marshes and scrub forests, the sanctuary provides a varied habitat that attracts a plethora of bird species. Notable inhabitants include migratory and resident birds such as flamingos, herons, and various shorebirds. The sanctuary plays a pivotal role in avian biodiversity conservation, with dedicated efforts towards preserving wetland habitats, managing human activities, and fostering awareness about bird conservation.")
            elif selected_wetland == "Gulf of Mannar Marine Biosphere Reserve":   
                st.title("Gulf of Mannar Marine Biosphere Reserve Overview")
                st.write("The Gulf of Mannar Marine Biosphere Reserve, situated between India and Sri Lanka, stands as a UNESCO Biosphere Reserve, recognized for its unparalleled marine diversity. The reserve's extensive coral reefs, seagrass beds, and mangroves contribute to its vital role in marine conservation. Beyond its natural wonders, the Gulf of Mannar holds significance in national and international protection initiatives, marking it as a sanctuary for diverse marine life.")
            elif selected_wetland == "Kanjirankulam Bird Sanctuary":   
                st.title("Kanjirankulam Bird Sanctuary Overview")
                st.write("Nestled in the heart of Tamil Nadu, the Kanjirankulam Bird Sanctuary beckons birdwatchers and nature enthusiasts alike. Its diverse habitat, enriched with wetlands, serves as a haven for various migratory and resident bird species. Conservation efforts are diligently employed to safeguard the sanctuary's unique ecology, ensuring the continued flourishing of its avian residents.")    
            elif selected_wetland == "Karikili Bird Sanctuary":   
                st.title("Karikili Bird Sanctuary Overview" )
                st.write("The Karikili Bird Sanctuary in Tamil Nadu is a testament to the state's rich avian diversity. Providing a sanctuary for migratory birds, the habitat supports a delicate balance in its ecosystem. Conservation initiatives play a crucial role in preserving the sanctuary's unique biodiversity.")    
            elif selected_wetland == "Koonthankulam Bird Sanctuary":   
                st.title("Koonthankulam Bird Sanctuary Overview")
                st.write("Celebrated for its vibrant birdlife, the Koonthankulam Bird Sanctuary in Tamil Nadu captivates visitors, particularly birdwatchers. The sanctuary's wetland environment fosters a diverse array of bird species, making it a vital hub for conservation efforts and a serene retreat for nature enthusiasts.")    
            elif selected_wetland == "Pallikaranai Marshland":   
                st.title("Pallikaranai Marshland Overview")
                st.write("The Pallikaranai Marshland in Tamil Nadu stands as a significant wetland ecosystem, characterized by its unique marshy environment. This crucial habitat supports a myriad of flora and fauna, contributing to the region's ecological balance. Conservation endeavors focus on sustaining the marshland's diverse ecology.")    
            elif selected_wetland == "Pichavaram Mangrove":   
                st.title("Pichavaram Mangrove Overview")
                st.write("The Pichavaram Mangrove Forest in Tamil Nadu unfolds a mesmerizing tapestry of intricate mangrove trees. Beyond its scenic beauty, this biodiverse ecosystem plays a pivotal role in coastal conservation. The mangrove's resilience and unique features make it a crucial asset in preserving the coastal ecosystem.")    
            elif selected_wetland == "Point Calimere Wildlife and Bird Sanctuary":   
                st.title("Point Calimere Wildlife and Bird Sanctuary Overview")
                st.write("Tucked away in Tamil Nadu, the Point Calimere Wildlife and Bird Sanctuary beckon wildlife enthusiasts with its diverse offerings. Providing a habitat for an array of bird species, the sanctuary stands as a testament to conservation efforts, ensuring the continued thriving of its avian residents.")    
            elif selected_wetland == "Suchindram  Theroor wetland complex":   
                st.title("Suchindram Theroor wetland complex Overview")
                st.write("The Suchindram Theroor Wetland Complex in Tamil Nadu is a treasure trove of wetland ecosystems. Hosting various bird species, this complex plays an essential role in maintaining ecological balance. Conservation efforts strive to protect and sustain this unique wetland habitat.")    
            elif selected_wetland == "Udayamarthandapuram Bird Sanctuary":   
                st.title("Udayamarthandapuram Bird Sanctuary Overview")
                st.write("The Udayamarthandapuram Bird Sanctuary in Tamil Nadu stands out for its diverse avian inhabitants. Conservation initiatives focus on safeguarding the sanctuary's ecological integrity, ensuring a conducive environment for its avian residents.")    
            elif selected_wetland == "Vaduvur Bird Sanctuary":   
                st.title("Vaduvur Bird Sanctuary Overview")
                st.write("As one of the oldest bird sanctuaries in India, the Vedanthangal Bird Sanctuary in Tamil Nadu holds historical and ecological significance. Celebrated for its migratory bird population, the sanctuary serves as a testament to successful conservation efforts.")    
            elif selected_wetland == "Vellode Bird Sanctuary":   
                st.title("Vellode Bird Sanctuary Overview")
                st.write("The Vellode Bird Sanctuary in Tamil Nadu offers a haven for birdwatchers, showcasing diverse avian residents. Conservation initiatives prioritize the protection of the sanctuary's natural habitat, fostering a balanced ecosystem.")    
            elif selected_wetland == "Vembannur Wetland complex":   
                st.title("Vembannur Wetland Complex Overview")
                st.write("The Vembannur Wetland Complex in Tamil Nadu is renowned for its expansive wetland ecosystem. Supporting various bird species, conservation efforts aim to preserve the vitality of this critical habitat, contributing to the region's biodiversity.")    
   



    



with tab1:
    st.markdown("<h1 style='text-align:left; color: #fffff;'>What is a Wetland</h1>", unsafe_allow_html=True)
    st.write("A wetland is a land area that is saturated or flooded with water either permanently or seasonally. Inland wetlands include marshes, peatlands, lakes, rivers, floodplains, and swamps. Coastal wetlands include saltwater marshes, estuaries, mangroves, lagoons and even coral reefs. Fish ponds, rice paddies and salt pans are human-made wetlands.")
    st.image("https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/59509a0c-9f3a-4b93-879a-839598904189/debwa5z-a74583f6-7479-42fa-91d0-789a75ba84df.png/v1/fill/w_603,h_350,q_70,strp/glowing_wetlands_by_eleathyra_debwa5z-350t.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9Njk3IiwicGF0aCI6IlwvZlwvNTk1MDlhMGMtOWYzYS00YjkzLTg3OWEtODM5NTk4OTA0MTg5XC9kZWJ3YTV6LWE3NDU4M2Y2LTc0NzktNDJmYS05MWQwLTc4OWE3NWJhODRkZi5wbmciLCJ3aWR0aCI6Ijw9MTIwMCJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.OGJo0GmWC3NE2ZmSGsRAZSaviyVgK2RQ4-jZ3b521hg",width=500)
    st.title("Wetland Types and Characteristics")

    st.header("Swamps:")
    st.markdown("""
    **Definition:** Swamps are wetlands characterized by standing water, often with trees and shrubs dominating the landscape.  
    **Water Source:** Swamps are typically fed by surface water, such as rivers or lakes.  
    **Vegetation:** The presence of trees and woody vegetation distinguishes swamps from other wetlands.  
    **Examples:** The Florida Everglades in the United States is an example of a freshwater swamp.
    """)
    st.image("https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/6ff2ccfb-d302-4348-87bc-8b9568748e63/d2xmqep-2993028f-4a5c-4ad2-bc1d-f8c429ba7d00.jpg/v1/fill/w_560,h_350,q_70,strp/swamp_by_jjcanvas_d2xmqep-350t.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTA1MCIsInBhdGgiOiJcL2ZcLzZmZjJjY2ZiLWQzMDItNDM0OC04N2JjLThiOTU2ODc0OGU2M1wvZDJ4bXFlcC0yOTkzMDI4Zi00YTVjLTRhZDItYmMxZC1mOGM0MjliYTdkMDAuanBnIiwid2lkdGgiOiI8PTE2ODAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.8t7L_TV1y0GmsrxYkGszZzuebmnXxaopqx3pfXeCKEA",width=500)

    st.header("Marshes:")
    st.markdown("""
    **Definition:** Marshes are wetlands characterized by shallow, standing water with predominantly herbaceous vegetation (grasses, reeds, sedges).  
    **Water Source:** Marshes may be freshwater or saltwater and are often found at the edges of rivers, lakes, or coastal areas.  
    **Vegetation:** Marshes are dominated by non-woody plants, and they play a crucial role in filtering water and providing habitat for various species.  
    **Examples:** The Everglades in Florida and the Camargue in France are examples of marshes.
    """)
    st.image("https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/2ec303ef-847a-4057-ad2e-a6704a8c03db/dcyov15-35e603e3-19cf-4a4b-811d-0b07f2ad7362.png/v1/fill/w_700,h_334,q_70,strp/swamp_by_umbatman_dcyov15-350t.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9NzY0IiwicGF0aCI6IlwvZlwvMmVjMzAzZWYtODQ3YS00MDU3LWFkMmUtYTY3MDRhOGMwM2RiXC9kY3lvdjE1LTM1ZTYwM2UzLTE5Y2YtNGE0Yi04MTFkLTBiMDdmMmFkNzM2Mi5wbmciLCJ3aWR0aCI6Ijw9MTYwMCJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.XLPDVh-fqLx0FyfuEY8XHjg2QeeMagXjll1yisPi0tg",width=500)

    st.header("Bogs:")
    st.markdown("""
    **Definition:** Bogs are wetlands characterized by acidic, nutrient-poor conditions, and they are often dominated by sphagnum moss.  
    **Water Source:** Bogs are typically rain-fed and may have stagnant water.  
    **Vegetation:** Bogs have unique plant communities, including mosses, heaths, and carnivorous plants. The slow decomposition of organic matter contributes to the acidic conditions.  
    **Examples:** The Great Vasyugan Swamp in Russia is an example of a bog.
    """)
    st.image("https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/41829219-9167-4a4d-893a-dacb85fcb779/dfshkeu-b07d88d1-84dc-48e9-98c4-d52077df9757.jpg/v1/fit/w_414,h_276,q_70,strp/wetlands_by_empyrea1_dfshkeu-414w.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9NjgzIiwicGF0aCI6IlwvZlwvNDE4MjkyMTktOTE2Ny00YTRkLTg5M2EtZGFjYjg1ZmNiNzc5XC9kZnNoa2V1LWIwN2Q4OGQxLTg0ZGMtNDhlOS05OGM0LWQ1MjA3N2RmOTc1Ny5qcGciLCJ3aWR0aCI6Ijw9MTAyNCJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.Wg5pUiLT8sSMVOxgdFs9s9R-KMv4F9cQEfQmeReT3Ak",width=500)

    st.header("Fens:")
    st.markdown("""
    **Definition:** Fens are wetlands similar to bogs but are less acidic, often fed by groundwater with a higher nutrient content.  
    **Water Source:** Fens have a consistent water supply from groundwater or nearby rivers, resulting in less acidic conditions compared to bogs.  
    **Vegetation:** Fens support a variety of plant life, including sedges, grasses, and herbs, and they often have a more diverse flora compared to bogs.  
    **Examples:** The Biebrza National Park in Poland is an example of a fen.
    """)
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTH3RaWSGTQSaBGstxNN6oIjYKAQF-BAO3S4Q&usqp=CAU",width=500)
    st.markdown("""
    These wetland types play essential roles in maintaining biodiversity, supporting unique ecosystems, and providing valuable ecosystem services such as water filtration, flood control, and habitat for numerous plant and animal species.
    """)
    st.header("Tamil Nadu State Wetlands Website")
    st.write("Explore the official website of the Tamil Nadu government or its environment and forest department. They often provide information on biodiversity, wildlife sanctuaries, and conservation initiatives.")
    st.link_button("Go to official *government wetlands website*", "https://www.tnswa.org/wetlands-of-tamil-nadu")
    

