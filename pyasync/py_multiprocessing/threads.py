"""
This sample demonstrates using ThreadPoolExecutor to download landing page of sites
"""
import time
# noinspection PyCompatibility
from concurrent.futures import ThreadPoolExecutor as Executor

urls = ["google", "twitter", "facebook", "youtube", "pinterest", "tumblr", "instagram", "reddit",
        "flickr", "meetup", "classmates", "microsoft", "apple", "linkedin", "xing", "renren",
        "disqus", "snapchat", "twoo", "whatsapp"]

current_milli_time = lambda: int(round(time.time() * 1000))


def fetch(url):
    """
    This simply downloads the given url or fetch landing page from the given url
    :param url: website url
    :return: length of the landing page from the given url
    :rtype: str
    """
    from urllib import request, error

    try:
        data = request.urlopen(url).read()
        return "{}: length {}".format(url, len(data))
    except error.HTTPError as e:
        return "{}: {}".format(url, e)


# create a ThreadPoolExecutor instance and specify the number of workers required
with Executor(max_workers=8) as exe:
    template = "http://www.{}.com"
    start_time = current_milli_time()

    # jobs are created 1 for every url, the executor managers the delivery of jobs to the
    # no of threads specified above
    jobs = [exe.submit(fetch, template.format(u)) for u in urls]

    # this simply waits for all the threads to return
    results = [job.result() for job in jobs]

print("\n".join(results))
end_time = current_milli_time()
print("Finished in {} seconds".format(round((end_time - start_time) / 1000)))

# output we expect
# http://www.google.com: length 10294
# http://www.twitter.com: length 329386
# http://www.facebook.com: length 148882
# http://www.youtube.com: length 552414
# http://www.pinterest.com: length 84393
# http://www.tumblr.com: length 71614
# http://www.instagram.com: length 9555
# http://www.reddit.com: length 140775
# http://www.flickr.com: length 200732
# http://www.meetup.com: length 115658
# http://www.classmates.com: length 33657
# http://www.microsoft.com: HTTP Error 403: Forbidden
# http://www.apple.com: length 44303
# http://www.linkedin.com: length 43591
# http://www.xing.com: length 43326
# http://www.renren.com: length 18926
# http://www.disqus.com: length 4814
# http://www.snapchat.com: length 20924
# http://www.twoo.com: length 44906
# http://www.whatsapp.com: length 36265
