import boto3

# Connecting to Rekognition to analyze the image.
rekognition = boto3.client("rekognition")


def lambda_handler(event, context):
    """
    The event should tell me:
    - which S3 bucket the image is in
    - the exact file name of the image
    """

    # Grab the bucket and image name from the event.
    bucket = event["bucket"]
    photo = event["photo"]


    # Check if the image has anything unsafe in it (violence, weapons, etc).
    moderation_response = rekognition.detect_moderation_labels(
        Image={"S3Object": {"Bucket": bucket, "Name": photo}}
    )

    # Get the general objects in the image so I can look for dangerous ones.
    labels_response = rekognition.detect_labels(
        Image={"S3Object": {"Bucket": bucket, "Name": photo}},
        MaxLabels=50,
        MinConfidence=50
    )

    # Store any threats found here.
    threat_details = []


    # Look through the unsafe/explicit content Rekognition found.
    for item in moderation_response["ModerationLabels"]:
        name = item["Name"]
        confidence = item["Confidence"]
        threat_details.append(f"Moderation: {name} ({confidence:.1f}%)")


    # Keywords for objects I consider dangerous.
    danger_keywords = [
        "Gun", "Weapon", "Knife", "Fire", "Explosion", "Smoke",
        "Blood", "Accident", "Rifle", "Pistol"
    ]

    # Check if any of the objects Rekognition detected match the dangerous ones.
    for label in labels_response["Labels"]:
        if label["Name"] in danger_keywords:
            threat_details.append(f"Object: {label['Name']} ({label['Confidence']:.1f}%)")


    # If anything suspicious was found, return it. Otherwise the image is fine.
    if threat_details:
        return {
            "ThreatDetected": True,
            "ThreatDetails": threat_details
        }
    else:
        return {
            "ThreatDetected": False,
            "Message": "No obvious threats or unsafe content found."
        }
