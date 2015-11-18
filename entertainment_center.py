import fresh_tomatoes
import media
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://www.highdefdiscnews.com/screenshots/toy_story_3_10.png",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")  
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://i0.wp.com/theserviceworkshop.com/wp-content/uploads/2014/11/Avatar_by_oohorusoo.png",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
Ratatouille = media.Movie("Ratatouille",
                          "Remy (Patton Oswalt), a resident of Paris, appreciates good food and has quite a sophisticated palate. He would love to become a chef so he can create and enjoy culinary masterpieces to his heart's delight. The only problem is, Remy is a rat. When he winds up in the sewer beneath one of Paris' finest restaurants, the rodent gourmet finds himself ideally placed to realize his dream.","http://www.renders-graphics.com/image/upload/normal/4206_render_souris2_de_ratatouille.png",
                          "https://www.youtube.com/watch?v=niD-jahFURU")
ajab_prem_ki_ghazab_kahani = media.Movie("ajab prem ki ghazab kahani","Ajab Prem Ki Ghazab Kahani is a 2009 romantic comedy film. It stars Ranbir Kapoor and Katrina Kaif in lead roles.It's a love story without i love you.","http://t07.deviantart.net/HALjph2h4OIsyqp-h02-m1pdrh8=/300x200/filters:fixed_height%28100,100%29:origin%28%29/pre09/be63/th/pre/f/2014/270/2/5/ajab_prem_ki_ghazab_kahani_movie_folder_icon_by_sharatj-d80sv5m.png",
                             "https://www.youtube.com/watch?v=-Yd6UH5HbLA")
midnight_in_paris = media.Movie("Midnight in Paris","Gil Pender (Owen Wilson) is a screenwriter and aspiring novelist. Vacationing in Paris with his fiancee (Rachel McAdams), he has taken to touring the city alone. On one such late-night excursion, Gil encounters a group of strange -- yet familiar -- revelers, who sweep him along, apparently back in time, for a night with some of the Jazz Age's icons of art and literature. The more time Gil spends with these cultural heroes of the past, the more dissatisfied he becomes with the present.",
                     "http://1.bp.blogspot.com/-Z624wTyZRaA/T0cCEiI8luI/AAAAAAAABhc/QTNvYG-O-6k/s1600/midnight-in-paris-A.png",
                     "https://www.youtube.com/watch?v=FAfR8omt-CY")
iron_man = media.Movie("Iron Man","A billionaire industrialist and genius inventor, Tony Stark (Robert Downey Jr.), is conducting weapons tests overseas, but terrorists kidnap him to force him to build a devastating weapon. Instead, he builds an armored suit and upends his captors. Returning to America, Stark refines the suit and uses it to combat crime and terrorism.",
            "http://icons.iconseeker.com/png/fullsize/ironman/ironman-m-iii.png","https://www.youtube.com/watch?v=8hYlB38asDY")

movies = [toy_story,avatar,Ratatouille,ajab_prem_ki_ghazab_kahani,midnight_in_paris,iron_man]
fresh_tomatoes.open_movies_page(movies)

#avatar.show_trailer()


                    

