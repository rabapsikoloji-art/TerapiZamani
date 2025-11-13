# Turkish Clinic Management System - API Integration Guide

This document provides detailed information about API integrations for a Turkish clinic management system, covering payment processing and notification services.

---

## 1. İyzico Payment Gateway API

### Overview
İyzico is Turkey's leading payment gateway, licensed by the Banking Regulation and Supervision Agency (BDDK), specializing in secure online payment processing with support for Turkish Lira (TL) and local payment methods.

### Required Credentials
- **API Key**: Unique identifier for your merchant account
- **Secret Key**: Secret credential for encryption and request signing
- **Base URL**: Different URLs for sandbox and production environments

### Authentication Method
- **Type**: Enhanced Basic Authentication
- **Process**: Uses API key and secret key with additional encryption layers including:
  - PKI string generation
  - Base64 encoding
  - SHA-1 hashing
- **Security**: All requests must be made over HTTPS with encrypted authorization headers

### How to Obtain Credentials

#### Step 1: Account Creation
1. Register on the İyzico website
2. Apply for a **business or corporate account** (individual accounts don't provide API access)
3. Wait for merchant approval from İyzico

#### Step 2: Access API Keys
1. After approval, log into the İyzico merchant panel at `merchant.iyzipay.com`
2. Navigate to **Account Settings** → **API Keys**
3. Find your credentials under **Live Keys** for production

#### Step 3: Sandbox Testing
- For testing, use the sandbox environment at `sandbox-merchant.iyzipay.com`
- Sandbox base URL: `https://sandbox-api.iyzipay.com`
- Production base URL: `https://api.iyzipay.com`

### Implementation Example (PHP)
```php
$options = new \Iyzipay\Options();
$options->setApiKey("your_api_key_here");
$options->setSecretKey("your_secret_key_here");
$options->setBaseUrl("https://sandbox-api.iyzipay.com"); // For testing
// Change to "https://api.iyzipay.com" for production
```

### Official Documentation
- **Main Documentation**: https://docs.iyzico.com/en
- **API Authentication**: https://dev.iyzipay.com/en/api/auth
- **Developer Portal**: https://dev.iyzipay.com/en/api
- **GitHub Repositories**: https://github.com/iyzico (Contains API clients for Java, PHP, Python, Node.js)

### Important Notes
- Credentials are only visible once after approval - store them securely
- **Avoid adding spaces** when entering keys - this is a common error
- Set locale to **"TR"** for Turkey-specific transactions
- Currency must be set to **"TL"** (Turkish Lira)
- Ensure addresses include Turkish-specific details for compliance
- Supports marketplace features with sub-merchant management for complex clinic scenarios
- PCI-DSS compliant for secure payment processing

### Scopes/Permissions Required
- Payment authorization
- 3D Secure transactions
- Refund and cancellation operations
- Subscription management (if using recurring payments)

### Turkey-Specific Considerations
- Compliance with KVKK (Turkish data protection law)
- Support for Turkish installment payments
- Anti-fraud systems tailored for Turkish market
- Requires buyer identity number for certain transactions

---

## 2. SMS & WhatsApp Notification Services

### Recommended Provider: Netgsm

**Best for**: Healthcare clinics requiring both SMS and WhatsApp Business API integration with Turkish regulatory compliance.

#### Required Credentials
- **Username**: Your Netgsm subscriber number
- **Password**: API sub-user password
- **Originator (Sender Name)**: Approved SMS header or subscriber number

#### Authentication Method
- **Type**: Sub-user based authentication
- **Setup**: Requires creating a dedicated API sub-user account

#### How to Obtain Credentials

##### For SMS API:
1. Log into Netgsm Webportal
2. Navigate to **Abonelik İşlemleri** → **Alt Kullanıcı Hesapları**
3. Create a new sub-user designated as **"API user"**
4. Submit identity details matching official documents
5. Activate API access via **Abonelik İşlemleri** → **API İşlemleri**
6. Enable SMS service permissions
7. Configure approved sender name in the software

##### For WhatsApp Business:
1. Ensure you have a valid Turkish phone number (0850, 0212, or 0312 prefixes)
2. Create a Facebook Business Account
3. Create a Facebook Developer Account
4. Set up WhatsApp Business application
5. Contact Netgsm call center at **0850 303 0 303** to complete integration

#### Official Documentation
- **SMS API Documentation**: https://www.netgsm.com.tr/dokuman/#api-dok%C3%BCman%C4%B1
- **Knowledge Base**: https://bilgibankasi.netgsm.com.tr/sms/toplu-sms/api-ile-sms
- **WhatsApp Integration Guide**: https://bilgibankasi.netgsm.com.tr/bilgi-bankasi/whatsapp-business-api-entegrasyonu/
- **Developer Portal**: https://www.netgsm.com.tr/gelistiriciler/

#### Features
- SMS sending via API
- OTP (One-Time Password) for verification
- WhatsApp Business API integration
- Multi-agent support for customer service
- Integration with İleti Yönetim Sistemi (İYS) for compliance
- 24/7 customer support

#### Pricing
- SMS packages purchased separately
- WhatsApp Business API - contact for pricing
- No setup fees for API access

#### Important Notes
- Sub-user creation is **mandatory** for API access
- Sender names must be approved by Netgsm
- Complies with BTK (Information and Communication Technologies Authority) regulations
- KVKK compliant for data protection
- Supports Turkish language and phone number formats
- Password can be reset if forgotten via the web portal

---

### Alternative Provider 1: Twilio

**Best for**: International scalability with global reach, though requires BTK compliance setup for Turkey.

#### Required Credentials
- **Account SID**: Unique identifier for your Twilio account
- **Auth Token**: Secret key for API authentication
- **Phone Number**: Purchased Twilio phone number for sending messages

#### Authentication Method
- **Type**: HTTP Basic Authentication
- **Credentials**: Account SID as username, Auth Token as password

#### Official Documentation
- **SMS API**: https://www.twilio.com/docs/messaging
- **WhatsApp API**: https://www.twilio.com/docs/whatsapp/api
- **WhatsApp Tutorial**: https://www.twilio.com/docs/whatsapp/tutorial
- **WhatsApp Quickstart**: https://www.twilio.com/docs/whatsapp/quickstart

#### Pricing (2025)
- **SMS**: $0.0305 per message
- **Volume discounts available**
- Transparent pricing with no hidden fees

#### Features
- Unified API for SMS, MMS, and WhatsApp
- Sandbox environment for WhatsApp testing
- Rich media support (images, videos, location)
- Template messages for business-initiated conversations
- Webhook support for inbound messages
- Multi-language SDK support (Python, Node.js, Java, PHP, etc.)

#### Turkey Integration
- Available through viaSocket integration for Turkey-specific SMS workflows
- WhatsApp Business Platform partner
- Requires template approval for WhatsApp business messages
- 24-hour customer service window for WhatsApp replies

#### Important Notes
- Requires explicit user opt-in for WhatsApp
- Messages must comply with WhatsApp business policies
- Rate limits apply (monitor API responses)
- For Turkey, ensure BTK compliance for SMS
- WhatsApp requires registering a sender phone number

---

### Alternative Provider 2: Turkey SMS

**Best for**: Healthcare-specific features with deep Turkish market integration.

#### Required Credentials
- **API Key**: Unique authentication key
- **Secret Key**: For request signing
- API credentials obtained after account approval

#### Authentication Method
- **Type**: API key-based authentication
- **Documentation**: RESTful API with detailed endpoint specifications

#### Official Documentation
- **Healthcare Solutions**: https://turkeysms.com.tr/en/sektorler-sms-hastaneler-tip-klinikleri
- **SMS API Documentation**: https://turkeysms.com.tr/api-documentations/sms-api-english
- **Developer Resources**: Available on website

#### Features (Healthcare-Specific)
- **Appointment Reminders**: Automated SMS for scheduled appointments
- **Medical Updates**: Patient health status notifications
- **Urgent Alerts**: Critical health information delivery
- **OTP Authentication**: Secure patient portal login
- **KVKK Compliant**: Full compliance with Turkish data protection
- **High Reliability**: ISO-certified service with detailed reporting

#### Sample Messages
```
"Reminder: Your appointment at [Clinic Name] is scheduled for [Date] at [Time]."
"Your lab results are ready. Please log in to your patient portal."
"Important: Please take your medication [Name] at [Time]."
```

#### Pricing
- Contact provider for healthcare-specific pricing
- No additional API setup costs
- Volume-based pricing available

#### Important Notes
- Specialized for Turkish healthcare sector
- High deliverability rates with major Turkish carriers (Turkcell, Vodafone, Turk Telekom)
- 24/7 support for healthcare clients
- Supports integration with hospital management systems

---

### Alternative Provider 3: SMSala

**Best for**: Budget-conscious clinics with good notification capabilities.

#### Required Credentials
- **API Key**: Authentication credential
- **Username**: Account identifier

#### Authentication Method
- **Type**: API key authentication
- RESTful API integration

#### Official Documentation
- **Main Website**: https://smsala.com/bulk-sms-turkey/

#### Pricing
- Starting at **₺650 for 10,000 SMS credits**
- Cost-effective for moderate volume clinics
- OTP and bulk messaging packages available

#### Features
- 98.2% delivery rate
- 24/7 support
- Easy API integration
- Appointment reminder support
- Transactional SMS capabilities

#### Important Notes
- Strong for general business use
- May require customization for healthcare-specific features
- Good balance of cost and reliability

---

## 3. Service Comparison & Recommendations

### For Payment Processing
**Recommendation: İyzico** ✅
- Only Turkish payment gateway in the comparison
- Full compliance with Turkish banking regulations
- Supports Turkish Lira and local payment methods
- Extensive documentation and API clients
- Marketplace features for complex scenarios

### For SMS & WhatsApp Notifications
**Primary Recommendation: Netgsm** ✅

**Why Netgsm:**
- ✅ Supports **both SMS and WhatsApp Business API** in one platform
- ✅ Deep integration with Turkish telecommunications infrastructure
- ✅ BTK and KVKK compliant
- ✅ Excellent customer support in Turkish
- ✅ Proven track record with healthcare providers
- ✅ Competitive pricing with no hidden fees
- ✅ Easy sub-user management for API access

**Secondary Recommendation: Turkey SMS** (Healthcare-Specific)
- Specialized for healthcare/clinic use cases
- Pre-built templates for medical notifications
- Strong compliance with healthcare regulations
- Higher reliability guarantees

**For International Scalability: Twilio**
- Best if planning to expand outside Turkey
- More expensive but very reliable
- Extensive documentation and developer tools
- Requires additional setup for Turkish compliance

---

## 4. Implementation Priorities

### Phase 1: Payment Gateway
1. Register İyzico business account
2. Obtain API credentials after approval
3. Test in sandbox environment
4. Implement payment flows with Turkish Lira
5. Add 3D Secure support
6. Test with Turkish test cards

### Phase 2: SMS Notifications
1. Create Netgsm account
2. Set up API sub-user
3. Configure sender name approval
4. Implement appointment reminder flows
5. Add OTP for patient portal authentication
6. Test message delivery across carriers

### Phase 3: WhatsApp Integration
1. Set up WhatsApp Business Account
2. Complete Netgsm WhatsApp integration
3. Create message templates for approval
4. Implement appointment confirmations
5. Add two-way communication for patient inquiries
6. Monitor engagement metrics

---

## 5. Security & Compliance Checklist

### Turkish Regulatory Requirements
- ✅ **KVKK Compliance**: Data protection and privacy
- ✅ **BTK Regulations**: Telecommunications authority compliance
- ✅ **İYS Integration**: Message consent management system
- ✅ **BDDK**: Banking regulations for payment processing

### Best Practices
- Store all API credentials in environment variables or secure vaults
- Use HTTPS for all API communications
- Implement rate limiting to avoid abuse
- Log all transactions for audit trails
- Regular security audits of API integrations
- Obtain explicit patient consent for notifications
- Encrypt sensitive patient data in transit and at rest
- Regular credential rotation (every 90 days recommended)

---

## 6. Next.js Implementation Notes

### Environment Variables Setup
```bash
# .env.local
# İyzico
IYZICO_API_KEY=your_api_key_here
IYZICO_SECRET_KEY=your_secret_key_here
IYZICO_BASE_URL=https://api.iyzipay.com

# Netgsm
NETGSM_USERNAME=your_subscriber_number
NETGSM_PASSWORD=your_api_password
NETGSM_SENDER_NAME=your_approved_sender

# WhatsApp (via Netgsm)
WHATSAPP_PHONE_NUMBER=your_turkish_number
```

### Recommended npm Packages
- **İyzico**: `iyzipay` (official Node.js SDK)
- **HTTP Requests**: `axios` or native `fetch`
- **Environment Variables**: `dotenv` (built-in Next.js support)

### API Route Structure (Next.js 13+)
```
/app/api/
  /payment/
    /create/route.js
    /callback/route.js
  /notifications/
    /sms/route.js
    /whatsapp/route.js
```

---

## 7. Testing Resources

### İyzico Test Cards
- Test environment provides specific card numbers for testing various scenarios
- Documentation includes cards for successful payments, 3D Secure, and failed transactions

### Netgsm Testing
- Use sandbox credentials for development
- Test SMS delivery with your own phone number first
- WhatsApp sandbox available for testing before production

### Recommended Testing Workflow
1. Start with sandbox/test environments
2. Test all success and failure scenarios
3. Verify webhook handling
4. Test rate limiting and error handling
5. Conduct security testing
6. User acceptance testing with Turkish stakeholders
7. Gradual rollout to production

---

## 8. Support Contacts

### İyzico
- **Website**: https://www.iyzico.com/en/
- **Support**: Via merchant dashboard
- **Developer Community**: GitHub discussions

### Netgsm
- **Call Center**: 0850 303 0 303
- **Website**: https://www.netgsm.com.tr/
- **Knowledge Base**: https://bilgibankasi.netgsm.com.tr/

### Twilio
- **Support**: https://help.twilio.com/
- **Documentation**: https://www.twilio.com/docs

---

## Conclusion

This guide provides a comprehensive overview of API integrations for a Turkish clinic management system. The recommended stack (İyzico + Netgsm) offers the best balance of local compliance, features, and reliability for healthcare applications in Turkey.

**Key Takeaways:**
- İyzico is the clear choice for payment processing in Turkey
- Netgsm provides the most comprehensive SMS + WhatsApp solution
- All providers require careful credential management and security practices
- Turkish regulatory compliance (KVKK, BTK) is non-negotiable
- Healthcare-specific features should be prioritized for clinic notifications

For any questions or additional integration needs, consult the official documentation links provided throughout this document.

---

**Document Version**: 1.0  
**Last Updated**: October 23, 2025  
**Prepared for**: Turkish Clinic Management System - Next.js Implementation
