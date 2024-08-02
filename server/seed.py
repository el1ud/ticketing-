# #!/usr/bin/env python3

# # Standard library imports
# from random import randint, choice as rc

# # Remote library imports
# from faker import Faker

# # Local imports
# from app import app
# from models import db

# if __name__ == '__main__':
#     fake = Faker()
#     with app.app_context():
#         print("Starting seed...")
#         # Seed code goes here!



# from flask import Flask

# app = Flask (__name__)

# @app.route("/members")
# def members():
#     return {"members": ["Members1", "Members2", "Members3"]}

# if __name__ == "_main_":
# #     app.run()



# #!/usr/bin/env python3

# # Standard library imports
# from random import randint, choice as rc

# # Remote library imports
# from faker import Faker
# fake = Faker()
# import os

# # Local imports
# from app import app
# from models import db, User, Destination, Review

# def make_users():
#     print("Seeding users...") 
#     User.query.delete()
    
#     users = []
    
#     username = [fake.unique.first_name() for _ in range(20)]
#     email = [fake.email() for _ in range(20)]
#     password = [fake.password(length=8) for _ in range(20)]
#     print(username[0], email[0], password[0])
    
#     for i in range(20):
#         user = User(username=username[i], email=email[i], password=password[i])
#         users.append(user)
    
#     db.session.add_all(users)
#     db.session.commit()

# def get_images(filename):
#     image_path = os.path.join('uploads', filename)
#     return image_path

# def make_destinations():
#     print("Seeding Destinations...")
#     Destination.query.delete()
    
#     destinations = []
    
#     places = [
#   {
#     "name": "Maasai Mara National Reserve",
#     "location": "Narok, Kenya",
#     "description": "Famous for its spectacular wildlife, Maasai Mara National Reserve is home to the Big Five and hosts the annual Great Migration of wildebeest and zebra, a spectacle of nature.",
#     "link": "https://images.unsplash.com/photo-1621139261252-27d1a67449f4?q=80&w=1940&h=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
#   },
#   {
#     "name": "Diani Beach",
#     "location": "Diani Beach, Kenya",
#     "description": "Renowned for its pristine white sands, crystal-clear turquoise waters, and vibrant coral reefs, Diani Beach offers ideal conditions for beach holidays, snorkeling, and diving.",
#     "link": "https://images.unsplash.com/photo-1651860282131-e3257674ccd1?q=80&w=1940&h=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
#   },
#   {
#     "name": "Eiffel Tower",
#     "location": "Paris, France",
#     "description": "An iconic symbol of Paris, the Eiffel Tower offers breathtaking views of the city from its observation decks. It is a must-visit landmark for tourists and an architectural marvel.",
#     "link": "https://images.unsplash.com/photo-1583265266785-aab9e443ee68?q=80&w=1940&h=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
#   },
#   {
#     "name": "Mount Kenya",
#     "location": "Laikipia, Kenya",
#     "description": "The second highest mountain in Africa, Mount Kenya boasts diverse ecosystems ranging from equatorial rainforests to snow-capped peaks, attracting climbers and nature enthusiasts alike.",
#     "link": "https://images.unsplash.com/photo-1489392191049-fc10c97e64b6?q=80&w=1940&h=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
#   },
#   {
#     "name": "Sydney Opera House",
#     "location": "Sydney, Australia",
#     "description": "The Sydney Opera House is a world-renowned architectural masterpiece and a vibrant performance venue. It is an essential stop for tourists visiting Sydney.",
#     "link": "https://images.unsplash.com/photo-1526958977630-bc61b30a2009?q=80&w=1940&h=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
#   },
#   {
#     "name": "Niagara Falls",
#     "location": "Ontario, Canada",
#     "description": "Niagara Falls is a breathtaking natural wonder, known for its impressive waterfalls and scenic beauty. It offers boat tours, observation decks, and a range of activities for visitors.",
#     "link": "https://images.unsplash.com/photo-1489447068241-b3490214e879?q=80&w=1940&h=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
#   },
#   {
#     "name": "Lamu Old Town",
#     "location": "Lamu Island, Kenya",
#     "description": "A UNESCO World Heritage Site, Lamu Old Town is renowned for its well-preserved Swahili architecture, winding alleys, and rich cultural heritage dating back centuries.",
#     "link": "https://images.unsplash.com/photo-1711802536772-0ef59886bc1b?q=80&w=1940&h=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
#   },
#   {
#     "name": "Colosseum",
#     "location": "Rome, Italy",
#     "description": "The Colosseum is an ancient amphitheater in Rome, known for its grand architecture and historical significance. It is one of the most iconic landmarks in Italy.",
#     "link": "https://images.unsplash.com/photo-1610113359997-0757e2a3323d?q=80&w=1940&h=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
#   },
#   {
#     "name": "Anse Lazio",
#     "location": "Praslin, Seychelles",
#     "description": "Anse Lazio is a pristine beach on the island of Praslin in Seychelles, known for its powdery white sand and clear turquoise waters. It offers a tranquil setting surrounded by lush greenery and granite boulders.",
#     "link": "https://images.unsplash.com/photo-1624964649692-21d0e2c08b6c?q=80&w=1940&h=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
#   },
#   {
#     "name": "Windsor Golf & Country Club",
#     "location": "Nairobi, Kenya",
#     "description": "The Windsor Country Club is a prestigious resort full of  lush greenery in Nairobi, Kenya. It offers a tranquil escape from the bustling city, combining luxury accommodation with a championship golf course.",
#     "link": "https://images.unsplash.com/photo-1679682265886-593dd0be280d?q=80&w=1940&h=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
#   },
#   {
#     "name": "Ngong Racecourse",
#     "location": "Ngong Road, Nairobi, Kenya",
#     "description": "Established in 1906, the Royal Nairobi Golf Club is one of Kenya's oldest and most prestigious golf courses, known for its lush fairways and challenging layout.",
#     "link": "https://images.unsplash.com/photo-1516673699707-4f2a243fafaf?q=80&w=1940&h=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
#   },
#   {
#     "name": "Fairmont The Norfolk Hotel",
#     "location": "Nairobi, Kenya",
#     "description": "An iconic luxury hotel in Nairobi, Fairmont The Norfolk Hotel offers colonial architecture, elegant accommodations, and a rich history dating back to the early 20th century.",
#     "link": "https://images.unsplash.com/photo-1664780476492-fbb9fd277ce8?q=80&w=1940&h=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
#   },
#   {
#     "name": "Santorini",
#     "location": "Greece",
#     "description": "Santorini is a beautiful island in Greece known for its white-washed buildings, stunning sunsets, and crystal-clear waters. It is a popular destination for romantic getaways and picturesque views.",
#     "link": "https://images.unsplash.com/photo-1538364103462-024a43692f10?q=80&w=1940&h=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
#   },
#   {
#     "name": "Machu Picchu",
#     "location": "Cuzco, Peru",
#     "description": "Machu Picchu is an ancient Incan city set high in the Andes Mountains in Peru. It is renowned for its archaeological significance and breathtaking views.",
#     "link": "https://images.unsplash.com/photo-1526392060635-9d6019884377?q=80&w=1940&h=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
#   },
#   {
#     "name": "Karura Forest",
#     "location": "Nairobi, Kenya",
#     "description": "Karura Forest in Nairobi is a large urban green space popular for walking, cycling, and picnicking amid serene natural surroundings and scenic waterfalls.",
#     "link": "https://images.unsplash.com/photo-1509599589979-3b5a15d2816e?q=80&w=1940&h=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
#   },
#   {
#     "name": "Taj Mahal",
#     "location": "Agra, India",
#     "description": "The Taj Mahal is a stunning mausoleum built by Mughal Emperor Shah Jahan in memory of his beloved wife. It is renowned for its beautiful white marble architecture and intricate designs.",
#     "link": "https://images.unsplash.com/photo-1564507592333-c60657eea523?q=80&w=1940&h=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
#   },
#   {
#     "name": "Circle Art Gallery",
#     "location": "Nairobi, Kenya",
#     "description": "Circle Art Gallery specializes in contemporary African art, featuring cutting-edge artworks from across the continent and providing a platform for emerging artists.",
#     "link": "https://images.unsplash.com/photo-1558522195-e1201b090344?q=80&w=1940&h=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
#   },
#   {
#     "name": "Coral Coast",
#     "location": "Viti Levu, Fiji",
#     "description": "The Coral Coast in Fiji is renowned for its stunning coral reefs, pristine beaches, and vibrant marine life. It offers opportunities for snorkeling, diving, and exploring traditional Fijian villages.",
#     "link": "https://images.unsplash.com/photo-1603491497345-a569d2a2d823?q=80&w=1940&h=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
#   },
#   {
#     "name": "One Off Contemporary Art Gallery",
#     "location": "Nairobi, Kenya",
#     "description": "One Off Contemporary Art Gallery in Nairobi is known for its diverse collection of contemporary art and exhibitions, offering a dynamic space for art enthusiasts.",
#     "link": "https://images.unsplash.com/photo-1708118936268-6b206202ea28?q=80&w=1940&h=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
#   },
#   {
#     "name": "The Pyramids of Giza",
#     "location": "Giza, Egypt",
#     "description": "The Pyramids of Giza are one of the Seven Wonders of the Ancient World. They are an incredible feat of engineering and a testament to ancient Egyptian civilization.",
#     "link": "https://images.unsplash.com/photo-1628503218283-6ddeac69dfea?q=80&w=1940&h=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
#   }
# ]

    
   
#     image_files = [get_images(f"Untitled design ({i}).png") for i in range(20)]
#     for i in range(len(places)):
#         destination = Destination(name = places[i].get('name'), description = places[i].get('description'), location = places[i].get('location'), image = image_files[i], link =  places[i].get('link'))
#         destinations.append(destination)
    
#     db.session.add_all(destinations)
#     db.session.commit()
    
# def make_reviews():
#     print("Seeding reviews...")
#     Review.query.delete()
    
#     review_list = []

#     reviews = [
        
        
#         ["Absolutely breathtaking experience! Saw the Big Five in one day.",
#         "Great safari trip, but the accommodations could be better.",
#         "Overpriced tours, but the scenery was worth it.",
#         "Amazing wildlife but encountered a lot of mosquitoes.",
#         "Loved the guides and their knowledge.",
#         "Disappointing experience overall."
#         ],
            
#         ["Beautiful beach with crystal-clear waters and white sand.",
#         "Litter on the beach was disappointing.",
#         "Perfect spot for relaxation and water sports."
#         ],
            
#         [
#         "Breathtaking views of Paris from the top!",
#         "Long queues but totally worth the wait.",
#         "A bit overpriced for the experience.",
#         "Absolutely loved the light show at night.",
#         "Amazing structure but very crowded.",
#         "Expected more for the price."
#         ],
        
#         ["Incredible trekking experience with stunning views.",
#         "Weather conditions made the summit unreachable this time.",
#         "Difficult hike, but the guides were helpful.",
#         "Base camps were lacking in amenities."],
#         [
#         "An incredible piece of history. Stunning views!",
#         "Wear comfortable shoes, the hike is intense.",
#         "Too many tourists, but still a must-see.",
#         "Loved the cable car ride up to the wall.",
#         "Amazing experience but bring your own food.",
#         "Very crowded, but worth it for the history."
#         ],
        
#        [
#         "The falls are breathtaking, a must-see.",
#         "Very touristy but the views are worth it.",
#         "Loved the boat tour, got very wet!",
#         "Amazing natural wonder.",
#         "Beautiful but very crowded.",
#         "Expected more from the experience."
#         ],
        
#         ["Delicious local cuisine and friendly people.",
#         "Tourist crowds can detract from the authentic experience.",
#         "Quaint and charming town with unique architecture.",
#         "Limited options for accommodation."],
        
# #         [
# #         "Fascinating history, a must-see in Rome.",
# #         "Very crowded, but the history is worth it.",
# #         "Guided tour was very informative.",
# #         "Amazing structure but overpriced tickets.",
# #         "Loved the ancient history and architecture.",
# #         "Too many tourists, hard to enjoy."
# #         ],
        
# #        [
# #         "Absolutely stunning beach with crystal-clear waters.",
# #         "Great for swimming and snorkeling.",
# #         "Beautiful coral reefs and marine life.",
# #         "Loved the sunset views from the beach.",
# #         "Peaceful and secluded, perfect for relaxation.",
# #         "A bit crowded during peak tourist season."
# #         ],
        
# #         ["Fantastic course with well-maintained greens.",
# #         "Facilities are aging and could use an update.",
# #         "Friendly staff and a relaxing atmosphere."],
        
# #         ["Affordable entertainment for families.",
# #         "Limited seating options for general admission.",
# #         "Parking can be chaotic during events.",
# #         "Exciting races and a lively atmosphere."],
        
# #         ["Historic hotel with elegant decor.",
# #         "Pricey dining options compared to local alternatives.",
# #         "Rooms were a bit noisy due to street traffic.",
# #         "Luxurious stay with impeccable service."],
# #         [
# #         "The sunsets are absolutely breathtaking.",
# #         "Beautiful island, but very crowded.",
# #         "Loved the white-washed buildings and blue domes.",
# #         "Overpriced but worth it for the views.",
# #         "Amazing food and friendly locals.",
# #         "Too touristy for my taste."
# #         ],
        
# #         [
# #         "An incredible experience, a must-see!",
# #         "The hike was tough but rewarding.",
# #         "Amazing views but very crowded.",
# #         "Loved the history and the guided tour.",
# #         "Expensive but worth every penny.",
# #         "Too many tourists, but the views are stunning."
# #         ],
        
# #         ["Great for picnics and bird watching.",
# #         "Some areas felt unsafe due to poor lighting.",
# #         "Serene walking trails and beautiful waterfalls.",
# #         "Entrance fees for non-residents are too high."],
# #         [
# #         "Absolutely stunning, worth the visit.",
# #         "Very crowded but a must-see.",
# #         "Loved the guided tour, very informative.",
# #         "Beautiful architecture but too many tourists.",
# #         "A magnificent piece of history.",
# #         "Expected more from the experience."
# #         ],
        
# #         ["Friendly and knowledgeable staff.",
# #         "Limited parking available nearby.",
# #         "Artworks were overpriced for the local market.",
# #         "Cutting-edge contemporary art showcased beautifully."],
# #        [
# #         "Amazing coral reefs and colorful marine life.",
# #         "Crystal-clear waters, perfect for snorkeling.",
# #         "Loved the traditional Fijian culture and hospitality.",
# #         "Great beachfront resorts with stunning views.",
# #         "Sunset views over the Coral Coast are breathtaking.",
# #         "A bit remote, but worth the journey."
# #         ],
        
# #         ["Gallery space felt too small for the exhibits.",
# #         "Lack of information about the artists on display.",
# #         "Great for art enthusiasts seeking something different."],
        
# #         [
# #         "Awe-inspiring and full of history.",
# #         "Very hot, bring lots of water.",
# #         "Too many tourists but a must-see.",
# #         "Loved the camel ride around the pyramids.",
# #         "Incredible experience, highly recommend.",
# #         "Overcrowded and very commercialized."
# #         ],
# #     ]
# #     ratings = [
# #         [5, 4, 2, 5, 3, 3],
# #         [5, 2, 5],
# #         [5, 4, 3, 5, 4, 3],
# #         [5, 2, 4, 3],
# #         [5, 5, 3, 4, 5, 3],
# #         [5, 4, 5, 5, 4, 3],
# #         [5, 3, 5, 2],
# #         [5, 5, 5, 5, 5, 4],
# #         [5, 4, 5, 3, 5, 3],
# #         [5, 3, 4],
# #         [4, 2, 3, 5],
# #         [4, 3, 2, 5],
# #         [5, 4, 5, 4, 5, 3],
# #         [5, 5, 4, 5, 4, 3],
# #         [4, 2, 5, 3],
# #         [5, 4, 5, 3, 5, 3],
# #         [2, 4, 3, 5],
# #         [5, 5, 5, 4, 5, 4],
# #         [1, 2, 5],
# #         [5, 4, 3, 5, 5, 3]
# #     ]
    
# #     for rev in range(len(ratings)):
# #         for i in range(len(reviews[rev])):
# #             review = Review(user_id = randint(1, 20), destination_id = rev+1, rating = ratings[rev][i], comment = reviews[rev][i], date = fake.date_this_decade())
# #             review_list.append(review)

# #     db.session.add_all(review_list)
# #     db.session.commit()

     
# # if __name__ == '__main__':
# #     with app.app_context():
# #         print("Starting seed..."),
# #         make_destinations(), 
# #         make_users(),
# #         make_reviews()
# #         print("Seeding complete!")


# from datetime import datetime
# from models import db
# from models import User, Concert, Ticket, ConcertUser

# # Drop all tables and recreate them (use with caution)
# db.drop_all()
# db.create_all()

# # Create Users
# user1 = User(username='john_doe', email='john@example.com')
# user1.set_password('password123')

# user2 = User(username='jane_smith', email='jane@example.com')
# user2.set_password('securepass')

# user3 = User(username='alice_jones', email='alice@example.com')
# user3.set_password('alicepassword')

# # Add users to session
# db.session.add_all([user1, user2, user3])
# db.session.commit()

# # Create Concerts with Images
# concert1 = Concert(name='Rock Fest', date=datetime(2024, 9, 15), venue='Stadium A', image_url='https://example.com/rockfest.jpg')
# concert2 = Concert(name='Jazz Night', date=datetime(2024, 10, 1), venue='Jazz Club B', image_url='https://example.com/jazznight.jpg')
# concert3 = Concert(name='Classical Evening', date=datetime(2024, 11, 20), venue='Opera House C', image_url='https://example.com/classicalevening.jpg')

# # Add concerts to session
# db.session.add_all([concert1, concert2, concert3])
# db.session.commit()

# # Create Tickets
# ticket1 = Ticket(seat_number='A1', price=50.00, user_id=user1.id, concert_id=concert1.id)
# ticket2 = Ticket(seat_number='B2', price=40.00, user_id=user2.id, concert_id=concert2.id)
# ticket3 = Ticket(seat_number='C3', price=30.00, user_id=user3.id, concert_id=concert3.id)
# ticket4 = Ticket(seat_number='D4', price=60.00, user_id=user1.id, concert_id=concert3.id)

# # Add tickets to session
# db.session.add_all([ticket1, ticket2, ticket3, ticket4])
# db.session.commit()

# # Create Concert-User Associations with Ratings
# concert_user1 = ConcertUser(user_id=user1.id, concert_id=concert1.id, user_rating=4.5)
# concert_user2 = ConcertUser(user_id=user2.id, concert_id=concert2.id, user_rating=4.8)
# concert_user3 = ConcertUser(user_id=user3.id, concert_id=concert3.id, user_rating=4.0)
# concert_user4 = ConcertUser(user_id=user1.id, concert_id=concert3.id, user_rating=5.0)

# # Add concert-user relationships to session
# db.session.add_all([concert_user1, concert_user2, concert_user3, concert_user4])
# db.session.commit()

# print("Database seeded successfully!")


# from datetime import datetime
# from flask import Flask
# from flask_migrate import Migrate
# from flask_bcrypt import Bcrypt
# from flask_jwt_extended import JWTManager
# #from models import app,db
# from models import User, Ticket, Concert, ConcertUser 

# # Local imports
# from config import app, db
# from models import db, User, Concert, Ticket, ConcertUser

# # Initialize Migrate and Bcrypt
# migrate = Migrate(app, db)
# bcrypt = Bcrypt(app)
# jwt = JWTManager(app)

# # Ensure the app context is available
# with app.app_context():
#     # Drop all tables and recreate them (use with caution)
#     db.drop_all()
#     db.create_all()

#     # Create Users
#     user1 = User(username='john_doe', email='john@example.com')
#     user1.set_password('password123')

#     user2 = User(username='jane_smith', email='jane@example.com')
#     user2.set_password('securepass')

#     user3 = User(username='alice_jones', email='alice@example.com')
#     user3.set_password('alicepassword')

#     # Add users to session
#     db.session.add_all([user1, user2, user3])
#     db.session.commit()

#     # Create Concerts with Images
#     concert1 = Concert(name='Rock Fest', date=datetime(2024, 9, 15), venue='Stadium A', image_url='https://example.com/rockfest.jpg')
#     concert2 = Concert(name='Jazz Night', date=datetime(2024, 10, 1), venue='Jazz Club B', image_url='https://example.com/jazznight.jpg')
#     concert3 = Concert(name='Classical Evening', date=datetime(2024, 11, 20), venue='Opera House C', image_url='https://example.com/classicalevening.jpg')

#     # Add concerts to session
#     db.session.add_all([concert1, concert2, concert3])
#     db.session.commit()

#     # Create Tickets
#     ticket1 = Ticket(seat_number='A1', price=50.00, user_id=user1.id, concert_id=concert1.id)
#     ticket2 = Ticket(seat_number='B2', price=40.00, user_id=user2.id, concert_id=concert2.id)
#     ticket3 = Ticket(seat_number='C3', price=30.00, user_id=user3.id, concert_id=concert3.id)
#     ticket4 = Ticket(seat_number='D4', price=60.00, user_id=user1.id, concert_id=concert3.id)

#     # Add tickets to session
#     db.session.add_all([ticket1, ticket2, ticket3, ticket4])
#     db.session.commit()

#     # Create Concert-User Associations with Ratings
#     concert_user1 = ConcertUser(user_id=user1.id, concert_id=concert1.id, user_rating=4.5)
#     concert_user2 = ConcertUser(user_id=user2.id, concert_id=concert2.id, user_rating=4.8)
#     concert_user3 = ConcertUser(user_id=user3.id, concert_id=concert3.id, user_rating=4.0)
#     concert_user4 = ConcertUser(user_id=user1.id, concert_id=concert3.id, user_rating=5.0)

#     # Add concert-user relationships to session
#     db.session.add_all([concert_user1, concert_user2, concert_user3, concert_user4])
#     db.session.commit()

#     print("Database seeded successfully!")

from faker import Faker
from app import app, db  # Adjust import based on your app structure
from models import User, Concert, Ticket, ConcertUser

fake = Faker()

def seed_users(n=10):
    for _ in range(n):
        user = User(
            username=fake.user_name(),
            email=fake.email(),
            password_hash=fake.password()
        )
        user.set_password(fake.password())  # Use the set_password method
        db.session.add(user)
    db.session.commit()

def seed_concerts(n=5):
    for _ in range(n):
        concert = Concert(
            name=fake.company(),
            date=fake.date_time_this_year(),
            venue=fake.city(),
            image_url=fake.image_url()
        )
        db.session.add(concert)
    db.session.commit()

def seed_tickets(n=20):
    users = User.query.all()
    concerts = Concert.query.all()
    
    for _ in range(n):
        ticket = Ticket(
            seat_number=fake.word(),
            price=fake.random_number(digits=2),
            user_id=fake.random_element(elements=[user.id for user in users]),
            concert_id=fake.random_element(elements=[concert.id for concert in concerts])
        )
        db.session.add(ticket)
    db.session.commit()

def seed_concert_users(n=15):
    users = User.query.all()
    concerts = Concert.query.all()
    
    for _ in range(n):
        concert_user = ConcertUser(
            user_id=fake.random_element(elements=[user.id for user in users]),
            concert_id=fake.random_element(elements=[concert.id for concert in concerts]),
            user_rating=fake.random_number(digits=1)
        )
        db.session.add(concert_user)
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        seed_users()
        seed_concerts()
        seed_tickets()
        seed_concert_users()
        print("Database seeded!")
