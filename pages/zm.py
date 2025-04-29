from components.page_utils import render_commodity_page

soybean_meal_description = """
<style>
    .soybean-meal-hover {
      display: inline-block;
      transition: color 0.3s, text-shadow 0.3s;
      font-weight: bold;
      color: inherit;
    }

    .soybean-meal-hover:hover {
      color: #8B4513;
      text-shadow: 0 0 10px rgba(139, 69, 19, 0.8), 0 0 20px rgba(139, 69, 19, 0.6);
    }  
</style>

<div>
  <p>
    <span class="soybean-meal-hover">Soybean Meal</span> is a high-protein byproduct of soybean crushing, crucial for the global livestock and poultry industries:
    <ul>
      <li>Primary source of protein feed for cattle, pigs, and poultry</li>
      <li>Vital for meat and dairy production worldwide</li>
      <li>Exported heavily from major producers like the U.S. and Brazil</li>
    </ul>
    Soybean meal prices reflect agricultural productivity and global protein demand.  
    They are influenced by:
    <ul>
      <li>Livestock production trends and animal feed demand</li>
      <li>Weather conditions affecting soybean harvests</li>
      <li>Competition from alternative protein meals (e.g., rapeseed meal)</li>
      <li>Global trade flows and regional feedstock shortages</li>
    </ul>
    As a staple input in animal nutrition, soybean meal is a key driver of agricultural trade and food supply chains around the world.
  </p>
</div>
"""

render_commodity_page(
    page_title="Soybean Meal CBOT Analytics (ZM)",
    ticker="ZM=F",
    description_html=soybean_meal_description,
    image_path="images/donnie-rosie-_G_NeCgniUg-unsplash.jpg",  # Remplace par ton chemin réel pour la farine de soja
    image_caption="Soybean Harvest",
    line_color="#8B4513"  # Brun terre (SaddleBrown)
)