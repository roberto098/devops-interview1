
FROM eclipse-temurin:21.0.2_13-jdk-jammy

# STEP 1: Add the executable jar file in this container
#gebruik een basisimage van Java 17
FROM openjdk:17-jdk-alpine
#workdirectory
WORKDIR /app
#kopieer de jar naar de container
COPY build/libs/helloworld.jar /app/helloworld.jar
# STEP 2: Run the application when the container starts
CMD ["java", "-jar", "/app/helloworld.jar"]

