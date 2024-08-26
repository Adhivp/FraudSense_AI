import streamlit as st

st.set_page_config(
    page_title="Features",
    page_icon="images/favicon/favicon-32x32.png" 
)

# Title and Header
st.title("Features")

# Description
st.write(
    """
    These features help in identifying and classifying URLs, particularly in distinguishing phishing websites from legitimate ones. 
    The extracted features are categorized into three main groups:
    """
)

# Address Bar based Features
st.subheader("I. Address Bar Based Features")
st.write(
    """
    The address bar of a URL contains crucial information that can be used to detect phishing attempts. 
    Below are the features extracted from the address bar:
    """
)

st.markdown("**1. Domain (Domain)**")
st.write(
    """
    The domain is the central part of the URL that identifies the website. 
    Extracting the domain allows us to analyze its characteristics, such as whether it’s a known legitimate domain or a potential phishing domain.
    """
)

st.markdown("**2. Have_IP (Have_IP)**")
st.write(
    """
    Sometimes, phishing URLs use an IP address instead of a domain name to mask their identity. 
    If an IP address is found in the URL, it’s a strong indicator of a phishing attempt.
    """
)

st.markdown("**3. Have_At (@)**")
st.write(
    """
    The '@' symbol in a URL is often used in phishing attacks to trick users. 
    Everything before the '@' is ignored by the browser, and the real address follows the '@'. 
    Identifying the presence of this symbol can help detect phishing URLs.
    """
)

st.markdown("**4. URL_Length (URL_Length)**")
st.write(
    """
    Phishers often use long URLs to hide malicious content. 
    By measuring the length of the URL, we can determine whether it’s suspiciously long and potentially dangerous.
    """
)

st.markdown("**5. URL_Depth (URL_Depth)**")
st.write(
    """
    The depth of a URL is determined by the number of subdirectories it contains. 
    A deep URL path with multiple subdirectories may indicate a phishing site trying to obscure its true nature.
    """
)

st.markdown("**6. Redirection (Redirection)**")
st.write(
    """
    The presence of double slashes ('//') in the URL path can indicate a redirection. 
    If the slashes appear after the domain name, it could be a sign of a phishing attempt, as legitimate URLs typically use them only after the protocol.
    """
)

st.markdown("**7. https_Domain (https_Domain)**")
st.write(
    """
    Phishers may include 'http' or 'https' in the domain name to trick users into believing the site is secure. 
    Detecting this can help identify phishing sites masquerading as legitimate ones.
    """
)

st.markdown("**8. Tiny_URL (Tiny_URL)**")
st.write(
    """
    URL shortening services, like TinyURL, are often used by phishers to disguise malicious links. 
    Identifying shortened URLs can help in flagging potential phishing attempts.
    """
)

st.markdown("**9. Prefix/Suffix (Prefix/Suffix)**")
st.write(
    """
    The use of a dash ('-') in the domain name is uncommon in legitimate sites but often used by phishers to create misleading URLs. 
    Detecting this can help in identifying phishing domains.
    """
)

# Domain based Features
st.subheader("II. Domain Based Features")
st.write(
    """
    The domain itself holds several features that can be analyzed to determine the legitimacy of a website. 
    Here are the key domain-based features:
    """
)

st.markdown("**10. DNS_Record (DNS_Record)**")
st.write(
    """
    DNS records provide information about the domain's registration and ownership. 
    If a domain has no DNS record or an unrecognized one, it’s a strong indicator that the site might be phishing.
    """
)

st.markdown("**11. Web_Traffic (Web_Traffic)**")
st.write(
    """
    Legitimate websites typically have higher traffic, which can be measured through tools like Alexa rankings. 
    Low or nonexistent traffic is often a sign of a phishing site.
    """
)

st.markdown("**12. Domain_Age (Domain_Age)**")
st.write(
    """
    Phishing sites are often short-lived, so the age of a domain is an important feature. 
    Older domains are generally more trustworthy, while younger domains might be suspicious.
    """
)

st.markdown("**13. Domain_End (Domain_End)**")
st.write(
    """
    The end period of a domain is the time left before it expires. 
    Phishing domains usually have short end periods, as they are not intended to be maintained for long.
    """
)

# HTML & JavaScript based Features
st.subheader("III. HTML & JavaScript Based Features")
st.write(
    """
    Analyzing the HTML and JavaScript used on a website can reveal suspicious behavior typical of phishing attempts. 
    The following features are extracted from the content of the website:
    """
)

st.markdown("**14. iFrame (iFrame)**")
st.write(
    """
    IFrames can be used to embed content from another webpage. 
    Phishers use invisible IFrames to redirect users to malicious sites. 
    Detecting this can help in identifying phishing sites.
    """
)

st.markdown("**15. Mouse_Over (Mouse_Over)**")
st.write(
    """
    Phishers may use JavaScript to change the status bar’s content, displaying fake URLs to trick users. 
    Identifying such customization helps in spotting phishing attempts.
    """
)

st.markdown("**16. Right_Click (Right_Click)**")
st.write(
    """
    Disabling right-click prevents users from viewing the webpage’s source code, a common tactic used by phishers. 
    Detecting this can indicate a potentially malicious site.
    """
)

st.markdown("**17. Web_Forwards (Web_Forwards)**")
st.write(
    """
    Legitimate websites typically don’t have many redirects. 
    However, phishing sites often redirect users multiple times to obscure their true location. 
    Detecting excessive forwarding can help in identifying phishing sites.
    """
)
