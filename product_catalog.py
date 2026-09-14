from product_data import products
# TODO: Step 1 - Print out the products to see the data that you are working with.


# TODO: Step 2 - Create a list called customer_preferences and store the user preference in this list.


response = ""
while response != "N":
    print("Input a preference:")
    preference = input()
    # Add the customer preference to the list
    customer_preferences = {"durable"}
    response = input("Do you want to add another preference? (Y/N): ").upper()
  

# TODO: Step 3 - Convert customer_preferences list to set to eliminate duplicates.
customer_preferences = set(customer_preferences)



# TODO: Step 4 - Convert the product tags to sets in order to allow for faster comparisons.
converted_products = []




# TODO: Step 5 - Write a function to calculate the number of matching tags
def count_matches(product_tags, customer_tags):
    return len(set(product_tags) & set(customer_tags))




# TODO: Step 6 - Write a function that loops over all products and returns a sorted list of matches
def recommend_products(products, customer_tags):
    matches = []

    for product in products:
        match_count = count_matches(product["tags"], customer_tags)
        if match_count > 0:
            matches.append((product, match_count))

    return sorted(matches, key=lambda match: match[1], reverse=True)



# TODO: Step 7 - Call your function and print the results
recommendations = recommend_products(products, customer_preferences)

for product, match_count in recommendations:
    print(f"- {product['name']}")




# DESIGN MEMO (write below in a comment):
# 1. The core operations used in this block of code are loops. The loops I find are the most efficient way of sorting a list of this size. The loops are used to iterate through the products and count the number of matching tags for each product. The sorted function is then used to sort the matches based on the number of matching tags in descending order. This allows for a quick and efficient way to recommend products based on customer preferences.
# 2. The code would be slightly changed if there were over 1,000 products by implementing another variable to track assuming there are no additional tags. I would add an option to select a smaller group of the list by requesting if the user's order of inputted preferences is important. This would allow for a more efficient search based off which preferences show up first for each product instead of just giving results if it showed up at all. The user would receive the same list of products, but the products that closest match the order of listed preferences would appear first.
