title = input()
print("<h1>")
print(f"    {title}")
print("</h1>")

content = input()
print("<article>")
print(f"    {content}")
print("</article>")

comment = input()
while not comment == "end of comments":
    print("<div>")
    print(f"    {comment}")
    print("</div>")

    comment = input()